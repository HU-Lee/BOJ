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

	for i := 0; i < n; i++ {
		var x int
		fmt.Fscanln(reader, &x)

		a := x / 25
		b := x % 25 / 10
		c := x % 25 % 10 / 5
		d := x % 5

		fmt.Fprintf(writer, "%d %d %d %d\n", a, b, c, d)
	}
}