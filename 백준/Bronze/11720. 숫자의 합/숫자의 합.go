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

	var num string
	fmt.Fscanln(reader, &num)
	
	sum := 0
	for i := 0; i < n; i++ {
		sum += int(num[i]) - '0'
	}
	fmt.Fprintln(writer, sum);
}