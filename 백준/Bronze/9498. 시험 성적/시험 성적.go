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

	var score int
	fmt.Fscanln(reader, &score)

	switch score / 10 {
	case 10,9:
		fmt.Fprintln(writer, "A")
	case 8:
		fmt.Fprintln(writer, "B")
	case 7:
		fmt.Fprintln(writer, "C")
	case 6:
		fmt.Fprintln(writer, "D")
	default:
		fmt.Fprintln(writer, "F")
	}
}