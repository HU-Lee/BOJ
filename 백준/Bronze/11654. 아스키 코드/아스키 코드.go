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

	var l string

	fmt.Fscanln(reader, &l)
	fmt.Fprintln(writer, int32(l[0]))
}