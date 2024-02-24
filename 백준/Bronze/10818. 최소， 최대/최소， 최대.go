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

	num := make([]int, n)
	min := 100000000
	max := -100000000
	for i := range num {
		fmt.Fscan(reader, &num[i])
		if num[i] < min {
			min = num[i]
		}
		if num[i] > max {
			max = num[i]
		}
	}
	fmt.Fprintln(writer, min, max);
}