package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = make(map[int]int)

func solve(n int) int {
	if n == 1 {
		dic[1] = 1
	} else if n == 2 {
		dic[2] = 2
	} else if n == 3 {
		dic[3] = 4
	} else {
		if _, ok := dic[n]; !ok {
			dic[n] = solve(n-1) + solve(n-2) + solve(n-3)
		}
	}
	return dic[n]
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var x int
		fmt.Fscanln(reader, &x)
		fmt.Fprintln(writer, solve(x))
	}
}