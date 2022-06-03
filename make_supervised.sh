#!/bin/sh
focaltext  supervised \
	 -lr 0.01 \
     -epoch 300 \
     -loss focal \
     -dim 300 \
	 -wordNgrams 4 \
     -thread 4 \
	 -pretrainedVectors ~/tesis/word-embeddings/SUC/vec/embeddings-l-model.vec \
     -input train.txt \
     -output model
