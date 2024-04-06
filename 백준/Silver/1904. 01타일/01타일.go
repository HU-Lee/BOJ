package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = map[int]int{
	1: 1,
	2: 2,
} 

func dp(n int) int {
	if _, ok := dic[n]; ok {
		return dic[n]
	} else {
		dic[n] = (dp(n-1) + dp(n-2))%15746
		return dic[n]
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	fmt.Fprintln(writer, dp(n))
}