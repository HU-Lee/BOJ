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

	max := 0
	idx := 0
	for i := 1; i<=9; i++ {
		var a int
		fmt.Fscanln(reader, &a)
		if a > max {
			max = a
			idx = i
		}
	}

	fmt.Fprintln(writer, max)
	fmt.Fprintln(writer, idx)

}

// go run template.go
