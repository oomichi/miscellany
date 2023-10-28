package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:10000")
	if err != nil {
		panic(err)
	}
	defer conn.Close()
	sendMessage(conn)
}

func sendMessage(conn net.Conn) {
	fmt.Print("> ")

	stdin := bufio.NewScanner(os.Stdin)
	if stdin.Scan() == false {
		fmt.Println("Ciao ciao!")
		return
	}

	_, err := conn.Write([]byte(stdin.Text()))
	if err != nil {
		panic(err)
	}

	var response = make([]byte, 4*1024)
	_, err = conn.Read(response)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Server> %s \n", response)

	sendMessage(conn)
}
