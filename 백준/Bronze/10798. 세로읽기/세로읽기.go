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

	arr := make([]string, 15)

	for i := 0; i < 5; i++ {
		var s string
		fmt.Fscanln(reader, &s)

		for j := 0; j < len(s); j++ {
			arr[j] += string(s[j])
		}
	}
	all := ""
	for i := 0; i < len(arr); i++ {
		all += arr[i]
	}
	fmt.Fprintln(writer, all)
}