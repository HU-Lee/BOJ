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

	var a,b int

	fmt.Fscanf(reader, "%d %d" ,&a, &b)
	fmt.Fprintln(writer, (a+b)*(a-b))
}