package main

import (
	"bufio"
	"fmt"
	"os"
)

func is_pel(str string) string {
	rune_str := []rune(str)
	for idx, l := range rune_str[:len(str)/2] {
		if l != rune_str[len(str)-1-idx] {
			return "no"
		}
	}
	return "yes"
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var num string

	for  {
		fmt.Fscanln(reader, &num)
		if num == "0" {
			break
		}
		fmt.Fprintln(writer, is_pel(num))
	}
}
