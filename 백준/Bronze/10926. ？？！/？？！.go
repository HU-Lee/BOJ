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

	var n string
	fmt.Fscanln(reader, &n)

	fmt.Fprintln(writer, n + "??!")
}