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

	var s string
	fmt.Fscanln(reader, &s)

	dic := make(map[int]int)

	for idx, l := range s {
		val := int(l - 'a')
		if _, ok := dic[val]; !ok {
			dic[val] = idx
		}
	}
	for i:=0;i<26;i++{
		if i == 25 {
			if val,ok:=dic[i];ok{
				fmt.Fprintf(writer,"%d",val)
			} else {
				fmt.Fprintf(writer,"%d",-1)
			}			
		} else {
			if val,ok:=dic[i];ok{
				fmt.Fprintf(writer,"%d ",val)
			} else {
				fmt.Fprintf(writer,"%d ",-1)
			}
		}
	}
}