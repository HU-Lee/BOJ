package main

import (
	"bufio"
	"fmt"
	"os"
)

var dic = make(map[int]int)

func fibo(n int) int {
	if n <= 2 {
		dic[n] = n
		return dic[n]
	} else {
		if _, ok := dic[n]; !ok {
			dic[n] = (fibo(n-1) + fibo(n-2))%10007			
		}
		return dic[n]
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	fmt.Fprintln(writer, fibo(n))
}