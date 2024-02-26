package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = make(map[int]int)

func factorial(n int) int {
	if n == 0 {
		dic[n] = 1
	} else {
		dic[n] = n * factorial(n-1)
	}
	return dic[n]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n,k int
	fmt.Fscanf(reader, "%d %d", &n, &k)

	fmt.Fprintln(writer, factorial(n)/(factorial(k)*factorial(n-k)))
}