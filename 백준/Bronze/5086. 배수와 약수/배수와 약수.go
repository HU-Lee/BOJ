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

	for {
		var x,y int
		fmt.Fscanln(reader, &x, &y)

		if x == 0 && y == 0 {
			return
		}

		if x % y == 0 {
			fmt.Fprintln(writer, "multiple")
		} else if y % x == 0 {
			fmt.Fprintln(writer, "factor")
		} else {
			fmt.Fprintln(writer, "neither")
		}
	}
}