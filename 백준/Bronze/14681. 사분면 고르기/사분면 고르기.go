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

	var x int
	var y int

	fmt.Fscanln(reader, &x)
	fmt.Fscanln(reader, &y)

	if x > 0 && y > 0 {
		fmt.Fprintln(writer, "1")
	} else if x < 0 && y > 0 {
		fmt.Fprintln(writer, "2")
	} else if x < 0 && y < 0 {
		fmt.Fprintln(writer, "3")
	} else if x > 0 && y < 0 {
		fmt.Fprintln(writer, "4")
	}
}