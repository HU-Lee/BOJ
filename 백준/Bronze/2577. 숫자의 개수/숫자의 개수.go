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

	sum := 1
	for i := 0; i < 3; i++ {
		var n int
		fmt.Fscanln(reader, &n)
		sum *= n
	}

	dic := make(map[int]int)

	for sum != 0 {
		dic[sum%10]++
		sum /= 10
	}

	for i := 0; i < 10; i++ {
		fmt.Fprintln(writer, dic[i])
	}
}