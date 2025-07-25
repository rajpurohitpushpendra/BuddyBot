
# # backend/app/routes/chat.py
# from fastapi import APIRouter, Request
# from app.services.nlu import process_message

# router = APIRouter()

# @router.post("/chat")
# async def chat_endpoint(request: Request):
#     data = await request.json()
#     user_input = data.get("message", "")
#     response = process_message(user_input)
#     return {"response": response}


# # backend/app/services/nlu.py
# def process_message(message):
#     # Basic NLU: keyword-based intent detection (can be expanded later)
#     message = message.lower()
#     if "weather" in message:
#         return "Sure, I can help with the weather."
#     elif "remind" in message:
#         return "I can set a reminder for you."
#     else:
#         return "I didn't understand that. Could you rephrase?"


# // frontend/src/components/ChatInput.jsx
# import React, { useState } from 'react';

# const ChatInput = ({ onSend }) => {
#   const [input, setInput] = useState("");

#   const handleSubmit = (e) => {
#     e.preventDefault();
#     if (!input.trim()) return;
#     onSend(input);
#     setInput("");
#   };

#   return (
#     <form onSubmit={handleSubmit} className="flex gap-2">
#       <input
#         type="text"
#         value={input}
#         onChange={(e) => setInput(e.target.value)}
#         placeholder="Type your message..."
#         className="flex-1 p-2 border rounded"
#       />
#       <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
#         Send
#       </button>
#     </form>
#   );
# };

# export default ChatInput;


# // frontend/src/components/ChatBubble.jsx
# import React from 'react';

# const ChatBubble = ({ text, isUser }) => {
#   return (
#     <div
#       className={`p-3 m-2 rounded-lg w-fit max-w-[75%] ${
#         isUser ? "bg-blue-200 self-end" : "bg-gray-200 self-start"
#       }`}
#     >
#       {text}
#     </div>
#   );
# };

# export default ChatBubble;


# // frontend/src/components/ResponseCard.jsx
# import React from 'react';

# const ResponseCard = ({ message }) => {
#   return (
#     <div className="p-4 bg-white shadow rounded m-2">
#       <p>{message}</p>
#     </div>
#   );
# };

# export default ResponseCard;
