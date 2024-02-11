package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = make(map[int]int)

func factorial(n int) int {
	if n == 0 || n == 1 {
		dic[n] = 1
		return 1
	} else if val, exists := dic[n]; exists {
		return val
	} else {
		dic[n] = n * factorial(n-1)
		return dic[n]
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int

	fmt.Fscanln(reader, &n)

	fmt.Fprintln(writer, factorial(n));
}