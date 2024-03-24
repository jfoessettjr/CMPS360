package main

import (
	"fmt"
	"net/http"
)

func main() {
	// Define header function
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `
		  <html>
		    <head>
		      <title>Joel's Website</title>
			</head>
			<body>
			<h1>Welcome to the Gem City!</h1>
			<p>Fun fact: On April 8, 2024 Erie will be in path of totality of the solar eclipse</p>
			<img src ="https://www.discoverpi.com/assets/galleries/2023-Sponsors/_940xAUTO_fit_center-center_100_none/Gem-City-Dinor.png" height="200" width="250"/>
			</body>
		  </html>
		`)
	})

	// Sports Page
	http.HandleFunc("/sports", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `
		  <html>
		    <head>
			  <title>Sports</title>
			</head>
			<body>
			<h1>It's a Great Day for Hockey!</h1>
			<p>My favorite Team is the Pittsburgh Penguins and my favorite Player is Sidney Crosby</p>
			<img src ="https://9b16f79ca967fd0708d1-2713572fef44aa49ec323e813b06d2d9.ssl.cf2.rackcdn.com/1140x_a10-7_cTC/Canucks-Penguins-Hockey-8-1708089740.jpg" height="500" width="450"/>
			</body>
		  </html>
		`)
	})

	// Hobby Page
	http.HandleFunc("/hobby", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, `
			<html>
			  <head>
			    <title>Hobbies</title>
			  </head>
			  <body>
			  <h1>Music is my language!</h1>
			  <p>I love listening to music one of my favorite artists is Dream Theater </p>
			  <p>Dream Theater plays Progressive Metal</p>
			  <img src ="https://m.media-amazon.com/images/I/41sQen2pIUL._SX300_SY300_QL70_FMwebp_.jpg" height="250" width="250"/>
			  </body>
			</html>
		`)
	})

	//Start the service
	fmt.Println("Server listening on Port 8080")
	http.ListenAndServe(":8080", nil)
}
