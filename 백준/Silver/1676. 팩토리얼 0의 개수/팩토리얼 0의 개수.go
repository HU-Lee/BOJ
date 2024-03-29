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

	sum := 0
	for n > 0 {
		n = n / 5
		sum += n
	}
	fmt.Fprintln(writer, sum)
}