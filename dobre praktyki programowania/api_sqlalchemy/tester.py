import threading, requests, time

def wyslij_zadanie_do_api(img_url):
    start = time.time()
    response = requests.get(img_url)
    print(response.status_code)

    print(f"Czas przetwarzania: {time.time() - start} sekund\n")


api_urls = [
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https%3A%2F%2Fplus.unsplash.com%2Fpremium_photo-1687989651252-95a08490e711%3Fq%3D80%26w%3D1740%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1661601744086-90da03a674f6?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://images.unsplash.com/photo-1415035008535-7ecdfd6d45b8?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "http://127.0.0.1:8000/analyze_img?img_url=https://plus.unsplash.com/premium_photo-1682089574502-8cbf911527d3?q=80&w=1742&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            ]

# target = funkcja, którą wątek ma wykonać
# args = argumenty, które przekazujemy do tej funkcji (musi być krotką, stąd przecinek na końcu)


for i in range(20):
    t = threading.Thread(target=wyslij_zadanie_do_api, args=(api_urls[i],))
    t.start()





# def wykryj_osoby_na_zdjeciu(img_url):
#     response = requests.get(img_url)
#     arr = np.frombuffer(response.content, dtype=np.uint8)
#     img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
#
#     hog = cv2.HOGDescriptor()
#     hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#
#     boxes, weights = hog.detectMultiScale(img)
#
#     return {"people count": len(boxes)}


# print(wykryj_osoby_na_zdjeciu("https://images.unsplash.com/photo-1632214383655-752a25bddd29?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"))
