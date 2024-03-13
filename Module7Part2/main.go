package main

import (
	"net/http"
	"os"
	"io"
)

func main() {
	// Define the file path of the input file
	filePath := "pittsburgh.txt"

	// Define a handler function to serve the file
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Open the input file
		file, err := os.Open(filePath)
		if err != nil {
			http.Error(w, "Failed to open file", http.StatusInternalServerError)
			return
		}
		defer file.Close()

		// Set the appropriate content type header
		w.Header().Set("Content-Type", "text/plain")

		// Copy the file contents to the response writer
		_, err = io.Copy(w, file)
		if err != nil {
			http.Error(w, "Failed to write response", http.StatusInternalServerError)
			return
		}
	})

	// Start the web server
	http.ListenAndServe(":8080", nil)
}
