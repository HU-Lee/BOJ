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

	var a,b,v int
	fmt.Fscanf(reader, "%d %d %d", &a, &b, &v)

	if a == v {
		fmt.Fprintln(writer, 1)
	} else {
		fmt.Fprintln(writer, (v-a -1)/(a-b) +2)
	}
}