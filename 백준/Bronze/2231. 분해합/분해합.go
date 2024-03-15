package main

import (
	"bufio"
	"fmt"
	"os"
)

func crash(n int) int {
	sum := n
	for n > 0 {
		sum += n%10
		n = n / 10
	}
	return sum
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := n-54; i < n; i++ {
		if crash(i) == n {
			fmt.Fprintln(writer, i)
			return
		}
	}
	fmt.Fprintln(writer, 0)
}

// go run template.go
