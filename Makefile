all: kmeans kmeans_streaming
kmeans:kmeans.c
	gcc kmeans.c -D_FILE_OFFSET_BITS=64 -lm -o kmeans
kmeans_streaming:kmeans_streaming.c
	gcc kmeans_streaming.c -D_FILE_OFFSET_BITS=64 -lm  -o kmeans_streaming
  
