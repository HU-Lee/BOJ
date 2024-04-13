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

	dic := make(map[int64]int)

	for i := 0; i < n; i++ {
		var n int64
		fmt.Fscanln(reader, &n)
		dic[n] = dic[n] + 1  
	}

	m := 0
	ans := int64(0)
	for k, v := range dic {
		if v > m {
			m = v
			ans = k
		} else if v == m && k < ans {
			ans = k
		}
	}
	fmt.Fprintln(writer, ans)
}