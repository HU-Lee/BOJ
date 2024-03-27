package main

import (
	"bufio"
	"fmt"
	"os"
)


func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	minx, miny, maxx, maxy := 100000, 100000, -100000, -100000
	for i := 0; i < n; i++ {
		var a,b int
		fmt.Fscanln(reader, &a, &b)

		minx = min(minx, a)
		miny = min(miny, b)
		maxx = max(maxx, a)
		maxy = max(maxy, b)
	}

	fmt.Fprintln(writer, (maxx-minx) * (maxy-miny))
}