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
	fmt.Fscanln(reader, &x)

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var a,b int
		fmt.Fscanln(reader, &a, &b)
		x -= a * b
	}
	if x != 0 {
		fmt.Fprintln(writer, "No")
	} else {
		fmt.Fprintln(writer, "Yes")
	}
}