import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import ChatMessage from "@/components/ChatMessage";
import { Button } from "./ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";

const Chat = ({ isCollapsed }) => {

    return (
        <div className="h-full w-full flex-col justify-center">
            {isCollapsed && (
            <>
            <Tabs defaultValue="ai">
            <TabsList className="grid w-full grid-cols-2 h-10">
                <TabsTrigger value="ai">AI Chat</TabsTrigger>
                <TabsTrigger value="discussion">Discussion</TabsTrigger>
            </TabsList>
            <TabsContent value="ai">
            <ScrollArea style={{ height: 'calc(100vh - 68*4px)'}}>
                    <ChatMessage message={{user: "GPT", content: "What do you need help with?"}} id={3} />
                    <ChatMessage message={{user: "User", content: "I need help with my project"}} id={4} />    
                    <ChatMessage message={{user: "GPT", content: "What do you need help with?"}} id={3} />
                    <ChatMessage message={{user: "User", content: "I need help with my project"}} id={4} />
                    <ChatMessage message={{user: "GPT", content: "What do you need help with?"}} id={3} />
                    <ChatMessage message={{user: "User", content: "I need help with my project"}} id={4} />
                    <ChatMessage message={{user: "GPT", content: "Hello, how can I help you?"}} id={1} />
                    <ChatMessage message={{user: "User", content: "I need help with my project"}} id={2} />
                </ScrollArea>
            </TabsContent>
            <TabsContent value="discussion">
a
            </TabsContent>
            </Tabs>
            
            <div className="w-full flex items-center bg-muted h-18">
                <Input placeholder="Write your message here" className="m-2"/>
                <Button className="m-2">Send message</Button>
            </div>
            <div className="bg-muted text-center text-sm text-muted-foreground p-2 h-18">
            GPT might make mistakes. 
            </div>
            </>
            )}
            
        </div>
    )
}

export default Chat;