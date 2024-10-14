from motor.motor_asyncio import AsyncIOMotorClient

client: AsyncIOMotorClient = None
database = None

async def connect_db():
    global client, database
    client = AsyncIOMotorClient("mongodb+srv://adminuser:P%40ssword1234@food-order-app.ty0c8.mongodb.net/food_order_db?retryWrites=true&w=majority&appName=food-order-app")
    database = client["food_order_db"]

async def disconnect_db():
    client.close()
