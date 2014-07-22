#include <Python.h>
#include "HTS_engine.h"
#include "HTS_hidden.h"

/* HTS_Engine_return_generated_speech: return generated speech */
static PyObject* HTS_Engine_return_generated_speech(HTS_Engine * engine)
{
	size_t i;
	double x;
	short temp;
	HTS_GStreamSet *gss = &engine->gss;
	int wav_bytes=sizeof(short)*HTS_GStreamSet_get_total_nsamples(gss);
	char *wav=malloc(wav_bytes);

	for (i = 0; i < HTS_GStreamSet_get_total_nsamples(gss); i++) {
		x = HTS_GStreamSet_get_speech(gss, i);
		if (x > 32767.0)
			temp = 32767;
		else if (x < -32768.0)
			temp = -32768;
		else
			temp = (short) x;
	  memcpy(wav+i*sizeof(short),&temp,sizeof(short));
	}
	return PyByteArray_FromStringAndSize(wav,wav_bytes);
}
static PyObject *
hts_engine_python_synthesize(PyObject *self, PyObject *args)
{
	const char *model_filename;
	HTS_Engine engine;
	PyObject *full_label_list;
	int full_label_length;
	char **full_label_array;
	PyObject *PySampwidth,*PyFramerate,*PyChannels,*PyWav;
	PyObject *PyResult=PyTuple_New(4);
	int i;

	if (!PyArg_ParseTuple(args, "sO!", &model_filename,&PyList_Type, &full_label_list))
		return NULL;
	
	HTS_Engine_initialize(&engine);
	
	/* load HTS voices */
	if (HTS_Engine_load(&engine, (char**)&model_filename, 1) != TRUE) {
	  fprintf(stderr, "Error: HTS voices cannot be loaded.\n");
	  HTS_Engine_clear(&engine);
	  exit(1);
	}

	full_label_length=PyList_Size(full_label_list);
	full_label_array=malloc(sizeof(char*)*full_label_length);
	for(i=0;i<full_label_length;i++)
	{
		full_label_array[i]=PyBytes_AS_STRING(
			PyUnicode_AsEncodedString(
				PyList_GetItem(full_label_list, i), "utf-8","strict" 
				)
			);
	}
	
	/* synthesize */
	if (HTS_Engine_synthesize_from_strings(&engine, full_label_array,full_label_length) != TRUE) {
	  fprintf(stderr, "Error: waveform cannot be synthesized.\n");
	  HTS_Engine_clear(&engine);
	  exit(1);
	}

	PySampwidth=PyLong_FromLong(2);
	PyFramerate=PyLong_FromLong(
		HTS_Engine_get_sampling_frequency(&engine));
	PyChannels=PyLong_FromLong(1);
	PyWav=HTS_Engine_return_generated_speech(&engine);

	/* reset */
	HTS_Engine_refresh(&engine);
	/* free memory */
	HTS_Engine_clear(&engine);
	
	PyTuple_SetItem(PyResult,0,PySampwidth);
	PyTuple_SetItem(PyResult,1,PyFramerate);
	PyTuple_SetItem(PyResult,2,PyChannels);
	PyTuple_SetItem(PyResult,3,PyWav);
	
	return PyResult;
}

static PyMethodDef hts_engine_python_methods[] = {
	{"synthesize",  hts_engine_python_synthesize, METH_VARARGS,
	 "Synthesize a full label by the model."},
	{NULL, NULL, 0, NULL}		/* Sentinel */
};

static struct PyModuleDef hts_engine_python_module = {
   PyModuleDef_HEAD_INIT,
   "htsengine",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,	   /* size of per-interpreter state of the module,
				or -1 if the module keeps state in global variables. */
   hts_engine_python_methods
};

PyMODINIT_FUNC
PyInit_htsengine(void)
{
	return PyModule_Create(&hts_engine_python_module);
}