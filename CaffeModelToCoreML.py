import coremltools


caffe_model = ('myCaffeModel.caffemodel', 'deploy.prototxt')

labels = 'list.txt'

coreml_model = coremltools.converters.caffe.convert(
	caffe_model, 
	class_labels=labels, 
	image_input_names='data'
)


coreml_model.author = 'Gael Foppolo'
coreml_model.license = 'MIT'
coreml_model.short_description = "Guess this ... and this"

coreml_model.input_description['data'] = 'Input images to be classified'

coreml_model.output_description['prob'] = 'Probability of each classifier'
coreml_model.output_description['classLabel'] = 'Most likely name of recognized object on the image'

coreml_model.save('myCoreMLModel.mlmodel')
