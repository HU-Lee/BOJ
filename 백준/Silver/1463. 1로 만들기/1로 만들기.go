package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = make([]int, 1000001)

func dp(n int) int {
	if dic[n] != 0 {
		return dic[n]
	} else {
		if n == 1 {
			dic[n] = 0
			return 0
		} else if n <= 3 {
			dic[n] = 1
			return 1
		} else {
			val := dp(n-1) + 1
			if n%2 == 0 {
				val = min(val, dp(n/2) + 1)
			}
			if n%3 == 0 {
				val = min(val, dp(n/3) + 1)
			}
			dic[n] = val
			return dic[n]
		}
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