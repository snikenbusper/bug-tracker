import { createServer } from "http";
import { Server } from "socket.io";

const httpServer = createServer();
const io = new Server(httpServer, 
    {
        cors: 
        {
            origin:"*",
            methods:["GET", "POST"]
        },
        host:"localhost",
        port:"5050"

    });

console.log("INITIALIZING")


io.on("connection", (socket)=>
{
    console.log(socket.id)
    socket.on("message", (msg, id)=>
    {
        console.log("Server recieved : " + msg + " from :" + id);
        io.emit("server-message", msg, id);
        console.log("Message emited")
    })
});


/*io.on("message", (msg)=>
{
    console.log("RECIEVED MESSAGE")
});*/

httpServer.listen(5050);