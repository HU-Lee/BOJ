package main

import (
	"bufio"
	"fmt"
	"os"
)

func is_pel(str string) int {
	rune_str := []rune(str)
	for idx, l := range rune_str[:len(str)/2] {
		if l != rune_str[len(str)-1-idx] {
			return 0
		}
	}
	return 1
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var word string

	fmt.Fscanln(reader, &word)
	fmt.Fprintln(writer, is_pel(word))
}