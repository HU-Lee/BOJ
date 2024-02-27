package main

import (
	"bufio"
	"fmt"
	"os"
)

func is_valid(s string) bool {
	cnt := 0
	for _, i := range s {
		if i == '(' {
			cnt++
		} else {
			cnt--
		}
		if cnt < 0 {
			return false
		}
	}
	return cnt == 0
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var s string
		fmt.Fscanln(reader, &s)
		if is_valid(s) {
			fmt.Fprintln(writer, "YES")
		} else {
			fmt.Fprintln(writer, "NO")
		}

	}
}