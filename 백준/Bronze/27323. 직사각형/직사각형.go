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

	var a int
	fmt.Fscanln(reader, &a)
	var b int
	fmt.Fscanln(reader, &b)

	fmt.Fprintln(writer, a*b)
}