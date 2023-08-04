### 0. What is System Design?

The process of establishing system aspects such as modules, architecture, components and their interfaces, and data for a system based on specified requirements is known as system design. It is the process of identifying, creating, and designing systems that meet a company’s or organization’s specific objectives and expectations. Systems design is more about system’s analysis, architectural patterns, APIs, design patterns, and glueing it all together than it is about coding. Because your application will be able to handle the architectural load, designing your system adequately for the requirements of your application will eliminate unnecessary costs and maintenance efforts, as well as provide a better experience for your end-users.


### 1. How is Horizontal scaling different from Vertical scaling?

- Horizontal scaling refers to the addition of more computing machines to the network that shares the processing and memory workload across a distributed network of devices. In simple words, more instances of servers are added to the existing pool and the traffic load is distributed across these devices in an efficient manner.
- Vertical scaling refers to the concept of upgrading the resource capacity such as increasing RAM, adding efficient processors etc of a single machine or switching to a new machine with more capacity. The capability of the server can be enhanced without the need for code manipulation.


### 2.What do you understand by load balancing? Why is it important in system design?

Load balancing refers to the concept of distributing incoming traffic efficiently across a group of various backend servers. These servers are called server pools. Modern-day websites are designed to serve millions of requests from clients and return the responses in a fast and reliable manner. In order to serve these requests, the addition of more servers is required. In such a scenario, it is essential to distribute request traffic efficiently across each server so that they do not face undue loads. Load balancer acts as a traffic police cop facing the requests and routes them across the available servers in a way that not a single server is overwhelmed which could possibly degrade the application performance.

When a server goes down, the load balancer redirects traffic to the remaining available servers. When a new server gets added to the configuration, the requests are automatically redirected to it. Following are the benefits of load balancers:

    - They help to prevent requests from going to unhealthy or unavailable servers.
    - Helps to prevent resources overloading.
    - Helps to eliminate a single point of failure since the requests are routed to available servers whenever a server goes down.
    - Requests sent to the servers are encrypted and the responses are decrypted. It aids in SSL termination and removes the need to install X.509 certificates on every server.
    - Load balancing impacts system security and allows continuous software updates for accomodating changes in the system.


### 3. What do you understand by Latency, throughput, and availability of a system?

Performance is an important factor in system design as it helps in making our services fast and reliable. Following are the three key metrics for measuring the performance:

- Latency: This is the time taken in milliseconds for delivering a single message.
- Throughput: This is the amount of data successfully transmitted through a system in a given amount of time. It is measured in bits per second.
- Availability: This determines the amount of time a system is available to respond to requests. It is calculated: System Uptime / (System Uptime+Downtime)

### 4. What is Sharding?

Sharding is a process of splitting the large logical dataset into multiple databases. It also refers to horizontal partitioning of data as it will be stored on multiple machines. By doing so, a sharded database becomes capable of handling more requests than a single large machine. Consider an example - in the following image, assume that we have around 1TB of data present in the database, when we perform sharding, we divide the large 1TB data into smaller chunks of 256GB into partitions called shards.

### 5. How is sharding different from partitioning?

- Database Sharding - Sharding is a technique for dividing a single dataset among many databases, allowing it to be stored across multiple workstations. Larger datasets can be divided into smaller parts and stored in numerous data nodes, boosting the system’s total storage capacity. A sharded database, similarly, can accommodate more requests than a single system by dividing the data over numerous machines. Sharding, also known as horizontal scaling or scale-out, is a type of scaling in which more nodes are added to distribute the load. Horizontal scaling provides near-limitless scalability for handling large amounts of data and high-volume tasks.
- Database Partitioning - Partitioning is the process of separating stored database objects (tables, indexes, and views) into distinct portions. Large database items are partitioned to improve controllability, performance, and availability. Partitioning can enhance performance when accessing partitioned tables in specific instances. Partitioning can act as a leading column in indexes, reducing index size and increasing the likelihood of finding the most desired indexes in memory. When a large portion of one area is used in the resultset, scanning that region is much faster than accessing data scattered throughout the entire table by index. Adding and deleting sections allows for large-scale data uploading and deletion, which improves performance. Data that are rarely used can be uploaded to more affordable data storage devices.


### 6. How is performance and scalability related to each other?

A system is said to be scalable if there is increased performance is proportional to the resources added. Generally, performance increase in terms of scalability refers to serving more work units. But this can also mean being able to handle larger work units when datasets grow. If there is a performance problem in the application, then the system will be slow only for a single user. But if there is a scalability problem, then the system may be fast for a single user but it can get slow under heavy user load on the application.


### 7. What is Caching? What are the various cache update strategies available in caching?

Caching refers to the process of storing file copies in a temporary storage location called cache which helps in accessing data more quickly thereby reducing site latency. The cache can only store a limited amount of data. Due to this, it is important to determine cache update strategies that are best suited for the business requirements. Following are the various caching strategies available:

- Cache-aside: In this strategy, our application is responsible to write and read data from the storage. Cache interaction with the storage is not direct. Here, the application looks for an entry in the cache, if the result is not found, then the entry is fetched from the database and is added to the cache for further use. Memcached is an example of using this update strategy.
Cache-aside strategy is also known as lazy loading because only the requested entry will be cached thereby avoiding unnecessary caching of the data. Some of the disadvantages of this strategy are:
    - In cases of a cache miss, there would be a noticeable delay as it results in fetching data from the database and then caching it.
    - The chances of data being stale are more if it is updated in the database. This can be reduced by defining the time-to-live parameter which forces an update of the cache entry.
    - When a cache node fails, it will be replaced by a new, empty node which results in increased latency.
- Write-through: In this strategy, the cache will be considered as the main data store by the system and the system reads and writes data into it. The cache then updates the database accordingly as shown in the database.

    - The system adds or updates the entry in the cache.
    - The cache synchronously writes entries to the database. This strategy is overall a slow operation because of the synchronous write operation. However, the subsequent reads of the recently written data will be very fast. This strategy also ensures that the cache is not stale. But, there are chances that the data written in the cache might never be read. This issue can be reduced by providing appropriate TTL.
- Write-behind (write-back): In this strategy, the application does the following steps:
    - Add or update an entry in the cache
    - Write the entry into the data store asynchronously for improving the write performance. This is demonstrated in the image below:
The main disadvantage of this method is that there are chances of data loss if the cache goes down before the contents of the cache are written into the database.
- Refresh-ahead: Using this strategy, we can configure the cache to refresh the cache entry automatically before its expiration.
This cache strategy results in reduced latency if it can predict accurately what items are needed in future.
### 8. What are the various Consistency patterns available in system design?

Consistency from the CAP theorem states that every read request should get the most recently written data. When there are multiple data copies available, there arises a problem of synchronizing them so that the clients get fresh data consistently. Following are the consistency patterns available:

- *Weak consistency:* After a data write, the read request may or may not be able to get the new data. This type of consistency works well in real-time use cases like VoIP, video chat, real-time multiplayer games etc. For example, when we are on a phone call, if we lose network for a few seconds, then we lose information about what was spoken during that time.
- *Eventual consistency:* Post data write, the reads will eventually see the latest data within milliseconds. Here, the data is replicated asynchronously. These are seen in DNS and email systems. This works well in highly available systems.
- *Strong consistency:* After a data write, the subsequent reads will see the latest data. Here, the data is replicated synchronously. This is seen in RDBMS and file systems and are suitable in systems requiring transactions of data.

### 9. What do you understand by Content delivery network?

Content delivery network or in short CDN is a globally distributed proxy server network that serves content from locations close by to the end-users. Usually, in websites, static files like HTML, CSS, JS files, images and videos are served from CDN.

Using CDN in delivering content helps to improve performance:
  - Since users receive data from centres close to them as shown in the image below, they don't have to wait for long.
  - Load on the servers is reduced significantly as some of the responsibility is shared by CDNs.

There are two types of CDNs, they are:

  - Push CDNs: Here, the content is received by the CDNs whenever changes occur on the server. The responsibility lies in us for uploading the content to CDNs. Content gets updated to the CDN only when it is modified or added which in turn maximises storage by minimising the traffic. Generally, sites with lesser traffic or content work well using push CDNs.
  - Pull CDNs: Here new content is grabbed from the server when the first user requests the content from the site. This leads to slower requests for the first time till the content gets stored/cached on the CDN. These CDNs minimizes space utilized on CDN but can lead to redundant traffic when expired files are pulled before they are changed. Websites having heavy traffic work well when used with pull CDNs.



### 10. What do you understand by Leader Election?

In a distributed environment where there are multiple servers contributing to the availability of the application, there can be situations where only one server has to take lead for updating third party APIs as different servers could cause problems while using the third party APIs. This server is called the primary server and the process of choosing this server is called leader election. The servers in the distributed environment have to detect when the leader server has failed and appoint another one to become a leader. This process is most suitable in high availability and strong consistency based applications by using a consensus algorithm.


### 11. How do you answer system design interview questions?

- Ask questions to the interviewer for clarification: Since the questions are purposefully vague, it is advised to ask relevant questions to the interviewer to ensure that both you and the interviewer are on the same page. Asking questions also shows that you care about the customer requirements.
- Gather the requirements: List all the features that are required, what are the common problems and system performance parameters that are expected by the system to handle. This step helps the interviewer to see how well you plan, expect problems and come up with solutions to each of them. Every choice matters while designing a system. For every choice, at least one pros and cons of the system needs to be listed.
- Come up with a design: Come up with a high-level design and low-level design solutions for each of the requirements decided. Discuss the pros and cons of the design. Also, discuss how they are beneficial to the business.

The primary objective of system design interviews is to evaluate how well a developer can plan, prioritize, evaluate various options to choose the best possible solution for a given problem.


### 12. What are some of the design issues in distributed systems?

Following are some of the issues found in distributed systems:

- Heterogeneity: The Internet allows applications to run over a heterogeneous collection of computers and networks. There would be different types of networks and the differences are masked by the usage of standard Internet protocols for communicating with each other. This becomes an issue while designing distributed applications
- Openness: Openness represents the measure by which a system can be extended and re-implemented in different ways. In distributed systems, it specifies the degree to which new sharing services can be added and made available for client usage.
- Security: The information maintained in distributed systems need to be secure as they are valuable to the users. The confidentiality, availability and integrity of the distributed systems have to be maintained and this sometimes becomes a challenge.
- Scalability: A system is scalable if it remains effective when there is a significant increase in the request traffic and resources. Designing a distributed system involves planning well in advance how well the system can be made scalable under varying user loads.
- Failure Handling: In a distributed environment, the failures are partial, meaning if some components fail, others would still function. It becomes challenging to handle these failures as it involves identifying right components where the failures occur.



### 13. Design a global chat service like Whatsapp or a facebook messenger.

- What are some of the required features?
        Allow users to chat over the internet.
        Provide support for one-on-one and group chats.
        Messages need to be stored for better viewing.
        Messages need to be encrypted for security purposes.
- What are some of the common problems that can be encountered?
        What would happen to a message if it is sent without an internet connection?
        Will encrypting and decrypting increase the latency?
        How are the messages sent and notified to the device?
- Possible Tips for consideration:
        Split database schema into multiple tables such as user table, chat table, massage table etc.
        Make use of web sockets for bi-directional communication between the device and the server.
        Make use of push notifications for notifying the members even if they are online.



### 14. How do you design a URL shortening service like TinyURL or bit.ly?

TinyURL or bit.ly takes a long URL and generates a new unique short URL. These systems are also capable of taking the shortened URL and returning the original full URL.

- What are some of the Required Features?
    - Generate a short URL having a length shorter than the original URL.
    - Store the original URL and map it to the shortened one.
    - Allow redirects in the shortened URLs.
    - Support custom names for short URLs.
    - Handle multiple requests at the same time.
- What are some of the Common Problems encountered?
    - What if two users input the same custom URL?
    - What happens if there are more user load than expected?
    - How do you regulate the database storage space?
- Possible tips for consideration:
    - The concept of hashing can be used for linking original and new URLs.
    - REST API can be used for balancing high traffic and handling front-end communication.
    - Multithreading concept for handling multiple requests at the same time.
    - NoSQL databases for storing original URLs.


### 15. Design a forum-like systems like Quora, Reddit or HackerNews.

These sites are meant for posting questions and answering them, showing newsfeed highlighting popular questions based on tags and related topics.


- What are some of the Required Features?
    - Users should be able to create public posts and apply tags to them.
    - Posts should be sortable based on tags.
    - Post comments in real-time by users.
    - Display posts on newsfeed based on followed tags.
- What are some of the Common Problems encountered?
    - Should it be just a web application?
    - Where to store the uploaded images and links?
    - How can you determine the related tags?
    - How can you distribute posts across a server network?
- Possible tips for consideration:
    - Check on using SQL database for mapping relational data between users, posts, comments, likes, tags, posts etc.
    - Incorporate multithreading and load balancer for supporting high traffic.
    - Make use of sharding for distributing the data across different systems.
    - Incorporate machine learning algorithms for finding correlations between the tags.



### 16. Design Facebook’s newsfeed system.

Facebook’s newsfeed allows users to see what is happening in their friend's circle, liked pages and groups followed.

- What are some of the Required Features?
    - Generate newsfeed using posts from other system entities that the user follows.
    - Newsfeed posts can be of text, image, audio or video format.
    - Append new posts to the user’s newsfeed in close to real-time.
- What are some of the Common Problems encountered?
    - What happens if the new post sees a lot of latency to get appended to the news feed?
    - Can the algorithm handle sudden user load?
    - What posts should take priority for displaying in the news feed?
- Possible tips for consideration:
    - Evaluate the process of fanout for publishing posts to the followers
    - Check how sharding can be achieved efficiently for handling heavy user load. The feed data of a user shouldn't be put into multiple servers. Instead, sharding can be done on user ids.




### 17. Design a parking lot system?

- What are some of the Required Features?
    - The parking lot can have multiple levels where each level has multiple rows for parking spots.
    - The parking lot can support parking for cars, buses, motorcycles hence spots can be of multiple sizes.
    - Consider the parking lot capacity at the time of designing the system.
    - Design appropriate pricing for each parking spot.
- What are some of the Common Problems encountered?
    - What should happen to the parking lot system if every spot is occupied?
    - Assigning parking lot spots of smaller size to vehicles of a bigger size.
- Possible tips for consideration:
    - Think of an algorithm for assigning an appropriate parking spot to a vehicle.
    - Think of different entities required for designing the system.




### 18. How do you design a recommendation system?

Recommendation systems are used for helping users identify what they want efficiently by assisting them by offering various choices and alternatives based on their history or interests.

- What are some of the Required Features?
    - Discuss what kind of recommendation system is required - whether it is for movies, e-commerce websites, songs etc.
- What are some of the common problems encountered?
    - Figure out how to recommend fresh and relevant content in real-time.
- Possible tips for consideration:
    - Discuss how to use the Eval component for understanding the working of the system.
    - Discuss how to train a collaborative filtering approach.




### 19. Design an API Rate Limiter system for GitHub or Firebase sites.

API Rate Limiters limit the API calls that a service receives in a given time period for avoiding request overload. This question can start with the coding algorithm on a single machine to the distributed network.

- What are some of the Required Features?
    - What is the required request count per hour or second? Let us assume that the requirement can be 10 requests per second.
    - Should the limiter notify the user if the requests are blocked?
    - The limiter should handle traffic suitable according to the scale.
- What are some of the common problems encountered?
    - How to measure the requests per given time?
    - How to design the rate limiter for the distributed systems when compared to a local system?
- Possible tips for consideration:
    - Evaluate the usage of sliding time windows for avoiding hourly resets.
    - Try using a counter integer instead of a request for saving space.




### 20. How do you design global file storage and file sharing services like Google Drive, Dropbox etc?

    What are some of the Required Features?
        Users should be able to upload, delete, share and download files over the web.
        File updates should be synced across multiple devices.
    What are some of the common problems encountered?
        Where to store the files?
        How can you handle updates? Should the files be re-uploaded or does just the modified version has to be updated?
        How to handle updation of two documents at the same time?
    Possible tips for consideration:
        Consider using chunking for splitting files into multiple sections for supporting re-uploads of a particular section rather than the whole file.
        Make use of cloud storage for storing the files.


### 21. Design a type-ahead search engine service.

This service partially completes the search queries by displaying n number of suggestions for completing the query that the user intended to search.

    What are some of the Required Features?
        Service has to match partial queries with popularly searched queries.
        The system has to display n number of suggestions (say 5, for example) based on the written query.
        The suggestions have to be updated based on the query updation.
    What are some of the common problems encountered?
        How to update the suggestions without much latency?
        How to determine the most likely suggestion?
        Are the suggestions adapting to the user’s search results?
        When do the suggestions appear? Is it updated on the fly or once the user stops writing?
    Possible tips for consideration:
        Evaluate the usage of natural language processing for anticipating the next characters.
        Markov chain rule for ranking the probabilities of top queries.



### 22.  Design Netflix.

Netflix is a video streaming service.

- What are some of the Required Features?
    - Uninterrupted video streaming to be made available for the users.
    - Likes and reviews of videos.
    - Recommend new videos.
    - Support high traffic of users.
- What are some of the common problems encountered?
    - Is it acceptable to have lags while uploading videos?
    - What happens if many users are accessing the same video concurrently?
- Possible tips for consideration:
    - Make use of cloud technology to store and transmit video data
    - There are three components of Netflix: OC (Content Delivery Network), Backend database, Client device for accessing the application.



### 23. Design Tic-Tac-Toe game.

Tic-tac-toe game involves two players where one player chooses 0 and the other player chooses X for marking the cells. The player who fills a row/column/diagonal with their selected character wins.

- What are some of the Required Features?
    - Support 2 player game where one player can be a computer.
    - Design algorithm to calculate the win and loss results.
- What are some of the common problems encountered?
    - What happens if both players play optimally?
    - How to decide the winning strategy?
- Possible tips for consideration:
    - If one player is a computer, then make use of the rand() method for ensuring moves are completely random.



### 24. Design a traffic control system.

Generally, in a traffic control system, we see that the lights transition from RED To GREEN, GREEN to ORANGE and then to RED.

- What are some of the Required Features?
    - Transition traffic lights based on the conventions.
- What are some of the common problems encountered?
    - Determine the time interval for which the state of the traffic lights has to change.
    - What happens in worst-case scenarios where the state is wrongly shown?
- Possible tips for consideration:
    - Make use of state design patterns and scheduling algorithms for the transition of the state from one colour to another.



### 25.  Design Web Crawler.

The Web crawler is a search engine-related service like Google, DuckDuckGo and is used for indexing website contents over the Internet for making them available for every result.

- What are some of the Required Features?
    - Design and develop a Scalable service for collecting information from the entire web and fetching millions of web documents.
    - Fresh data has to be fetched for every search query.
- What are some of the common problems encountered?
    - How to handle the updates when users are typing very fast?
    - How to prioritize dynamically changing web pages?
- Possible tips for consideration:
    - Look into URL Frontier Architecture for implementing this system.
    - Know how crawling is different from scraping.



### 26. Design ATM system.

ATMs are used for depositing and withdrawing money from customers. It is also useful for checking the account balance.

- What are some of the required features?
    - Each user should have at least one bank account that is linked to the card for performing transactions.
    - ATM to authenticate the user based on 4 digit PIN associated with the card.
    - User to perform only one transaction at a given time.
- What are some of the common problems encountered?
    - What happens during transaction timeout?
    - What happens if the money is deducted from the bank account but the user hasn't received it from the machine?
- Possible tips for consideration:
    - Divide the problem into different entities like Card, Card Reader etc and establish a relationship between each of the entities.



### 27. Design Uber, Ola or Lyft type of systems.

These platforms help user request rides and the driver picks them up from the location and drop them at the destination selected by the user.

- What are some of the required features?
    - Real-time service for booking rides
    - Should have the capability of assigning rides that lets the user reach the destination fast.
    - Show the ETA (Estimated Time of Arrival) of the driver after booking the ride and once the ride has been started, show the ETA of the vehicle arriving at the destination.
- What are some of the common problems encountered?
    - How to store geographical locations for drivers always on move?
    - How to assign drivers to the customers efficiently?
    - How do you calculate the ETA of the driver arrival or the destination arrival?
- Possible tips for consideration:
    - Make use of the microservices concept with fast databases for booking rides faster.
    - Evaluate Dispatch System for assigning drivers to the users.


### 28. What is the network?

Network is usually an informally interconnected group or association of different entities like a person, computers, radio stations, etc.

### 29. Why is the computer network so important?
it allows connecting all different network-enabled devices which enable data and information sharing between them and that makes computer networks a core part of our life 

### 30. How are Network types classified?

Network types can be classified and divided based on the area of distribution of the network. 

### 31. Explain different types of networks.


- *PAN (Personal Area Network)*: 	Let devices connect and communicate over the range of a person. E.g. connecting Bluetooth devices.
- *LAN (Local Area Network)*: 	It is a privately owned network that operates within and nearby a single building like a home, office, or factory
- *MAN (Metropolitan Area Network)*: 	It connects and covers the whole city. E.g. TV Cable connection over the city
- *WAN (Wide Area Network)*: 	It spans a large geographical area, often a country or continent. The Internet is the largest WAN
- *GAN (Global Area Network)*: 	It is also known as the Internet which connects the globe using satellites. The Internet is also called the Network of WANs.

### 32. Explain LAN (Local Area Network)

LANs are widely used to connect computers/laptops and consumer electronics which enables them to share resources (e.g., printers, fax machines) and exchange information. When LANs are used by companies or organizations, they are called enterprise networks. There are two different types of LAN networks i.e. wireless LAN (no wires involved achieved using Wi-Fi) and wired LAN (achieved using LAN cable). Wireless LANs are very popular these days for places where installing wire is difficult. The below diagrams explain both wireless and wired LAN.

### 33. Tell me something about VPN (Virtual Private Network)

VPN or the Virtual Private Network is a private WAN (Wide Area Network) built on the internet. It allows the creation of a secured tunnel (protected network) between different networks using the internet (public network). By using the VPN, a client can connect to the organization’s network remotely. The below diagram shows an organizational WAN network over Australia created using VPN:

### 34. What are the advantages of using a VPN?

Below are few advantages of using VPN:

- VPN is used to connect offices in different geographical locations remotely and is cheaper when compared to WAN connections.
- VPN is used for secure transactions and confidential data transfer between multiple offices located in different geographical locations.
- VPN keeps an organization’s information secured against any potential threats or intrusions by using virtualization.
- VPN encrypts the internet traffic and disguises the online identity.



### 35. What are the different types of VPN?

Few types of VPN are:

- Access VPN: Access VPN is used to provide connectivity to remote mobile users and telecommuters. It serves as an alternative to dial-up connections or ISDN (Integrated Services Digital Network) connections. It is a low-cost solution and provides a wide range of connectivity.
- Site-to-Site VPN: A Site-to-Site or Router-to-Router VPN is commonly used in large companies having branches in different locations to connect the network of one office to another in different locations. There are 2 sub-categories as mentioned below:
- Intranet VPN: Intranet VPN is useful for connecting remote offices in different geographical locations using shared infrastructure (internet connectivity and servers) with the same accessibility policies as a private WAN (wide area network).
- Extranet VPN: Extranet VPN uses shared infrastructure over an intranet, suppliers, customers, partners, and other entities and connects them using dedicated connections.



### 36. What are nodes and links?

- *Node:* Any communicating device in a network is called a Node. Node is the point of intersection in a network. It can send/receive data and information within a network. Examples of the node can be computers, laptops, printers, servers, modems, etc.

- *Link:* A link or edge refers to the connectivity between two nodes in the network. It includes the type of connectivity (wired or wireless) between the nodes and protocols used for one node to be able to communicate with the other.

### 37.  What is the network topology?

Network topology is a physical layout of the network, connecting the different nodes using the links. It depicts the connectivity between the computers, devices, cables, etc.


### 38. Define different types of network topology

The different types of network topology are given below:

- Bus Topology:
    - All the nodes are connected using the central link known as the bus.
    - It is useful to connect a smaller number of devices.
    - If the main cable gets damaged, it will damage the whole network.

- Star Topology:
    - All the nodes are connected to one single node known as the central node.
    - It is more robust.
    - If the central node fails the complete network is damaged.
    - Easy to troubleshoot.
    - Mainly used in home and office networks.
  
- Ring Topology:
    - Each node is connected to exactly two nodes forming a ring structure
    - If one of the nodes are damaged, it will damage the whole network
    - It is used very rarely as it is expensive and hard to install and manage
  
- Mesh Topology:
    - Each node is connected to one or many nodes.
    - It is robust as failure in one link only disconnects that node.
    - It is rarely used and installation and management are difficult.

- Tree Topology:
    - A combination of star and bus topology also know as an extended bus topology.
    - All the smaller star networks are connected to a single bus.
    - If the main bus fails, the whole network is damaged.

### 39. What is an IPv4 address? What are the different classes of IPv4?

An IP address is a 32-bit dynamic address of a node in the network. An IPv4 address has 4 octets of 8-bit each with each number with a value up to 255.

IPv4 classes are differentiated based on the number of hosts it supports on the network. There are five types of IPv4 classes and are based on the first octet of IP addresses which are classified as Class A, B, C, D, or E.

### 40. What are Private and Special IP addresses?

- *Private Address:* For each class, there are specific IPs that are reserved specifically for private use only. This IP address cannot be used for devices on the Internet as they are non-routable.

- *Special Address:* IP Range from 127.0.0.1 to 127.255.255.255 are network testing addresses also known as loopback addresses are the special IP address.

|IPv4 Class |	Private IPv4 Start Address| 	Private IPv4 End Address|
|-|-|-|
|A |	10.0.0.0 |	10.255.255.255|
|B 	|172.16.0.0 |	172.31.255.255|
|C |	192.168.0.0 	|192.168.255.255|
### 41. Describe the OSI Reference Model

Open System Interconnections (OSI) is a network architecture model based on the ISO standards. It is called the OSI model as it deals with connecting the systems that are open for communication with other systems.

The OSI model has seven layers. The principles used to arrive at the seven layers can be summarized  briefly as below:

- Create a new layer if a different abstraction is needed.
- Each layer should have a well-defined function.
- The function of each layer is chosen based on internationally standardized protocols.



### 42. Define the 7 different layers of the OSI Reference Model
|Layer |	Unit Exchanged |	Description | 
|-|  ------------ |--------|
|Physical 	|Bit | It is concerned with transmitting raw bits over a communication channel.  Chooses which type of transmission mode is to be selected for the transmission. The available transmission modes are Simplex, Half Duplex and Full Duplex.,|
|Data  Link | 	Frame 	| The main task of this layer is to transform a raw transmission facility into a line that appears free of undetected transmission errors. It also allows detecting damaged packets using the CRC (Cyclic Redundancy Check) error-detecting, code. When more than one node is connected to a shared link, Data Link Layer protocols are required to determine which device has control over the link at a given time. It is implemented by protocols like CSMA/CD, CSMA/CA, ALOHA, and Token Passing.|
|Network| 	Packet 	|It controls the operation of the subnet. The network layer takes care of feedback messaging through ICMP messages.|
|Transport| 	TPDU - Transaction Protocol Data Unit| 	The basic functionality of this layer is to accept data from the above layers, split it up into smaller units if needed, pass these to the network layer, and ensure that all the pieces arrive correctly at the other end. The Transport Layer takes care of Segmentation and Reassembly.|
|Session| 	SPDU - Session Protocol Data Unit| 	 The session layer allows users on different machines to establish sessions between them. Dialogue control is using the full-duplex link as half-duplex. It sends out dummy packets from the client to the server when the client is ideal.|
|Presentation| 	PPDU - Presentation Protocol Data Unit|The presentation layer is concerned with the syntax and semantics of the information transmitted. It translates a message from a common form to the encoded format which will be understood by the receiver.|
|Application| 	APDU - Application Protocol Data Unit| 	 It contains a variety of protocols that are commonly needed by users. The application layer sends data of any size to the transport layer.|


### 43. Describe the TCP/IP Reference Model

It is a compressed version of the OSI model with only 4 layers. It was developed by the US Department of Defence (DoD) in the 1980s. The name of this model is based on 2 standard protocols used i.e. TCP (Transmission Control Protocol) and IP (Internet Protocol).

- *Link :*	Decides which links such as serial lines or classic Ethernet must be used to meet the needs of the connectionless internet layer.
- *Internet*: 	
    - The internet layer is the most important layer which holds the whole architecture together.
    - It delivers the IP packets where they are supposed to be delivered.

- *Transport*: 	Its functionality is almost the same as the OSI transport layer. It enables peer entities on the network to carry on a conversation.
- *Application*: 	It contains all the higher-level protocols.

### 44. What are the HTTP and the HTTPS protocol?

- HTTP is the HyperText Transfer Protocol which defines the set of rules and standards on how the information can be transmitted on the World Wide Web (WWW).  It helps the web browsers and web servers for communication. It is a ‘stateless protocol’ where each command is independent with respect to the previous command. HTTP is an application layer protocol built upon the TCP. It uses port 80 by default.

- HTTPS is the HyperText Transfer Protocol Secure or Secure HTTP. It is an advanced and secured version of HTTP. On top of HTTP, SSL/TLS protocol is used to provide security. It enables secure transactions by encrypting the communication and also helps identify network servers securely. It uses port 443 by default.


### 45. What is the SMTP protocol?

SMTP is the Simple Mail Transfer Protocol. SMTP sets the rule for communication between servers. This set of rules helps the software to transmit emails over the internet. It supports both End-to-End and Store-and-Forward methods. It is in always-listening mode on port 25.

### 46. What is the DNS?

DNS is the Domain Name System. It is considered as the devices/services directory of the Internet. It is a decentralized and hierarchical naming system for devices/services connected to the Internet. It translates the domain names to their corresponding IPs. For e.g. interviewbit.com to 172.217.166.36. It uses port 53 by default.


### 47. What is the use of a router and how is it different from a gateway?

The router is a networking device used for connecting two or more network segments. It directs the traffic in the network. It transfers information and data like web pages, emails, images, videos, etc. from source to destination in the form of packets. It operates at the network layer. The gateways are also used to route and regulate the network traffic but, they can also send data between two dissimilar networks while a router can only send data to similar networks.


### 48. What is the TCP protocol?

TCP or TCP/IP is the Transmission Control Protocol/Internet Protocol. It is a set of rules that decides how a computer connects to the Internet and how to transmit the data over the network. It creates a virtual network when more than one computer is connected to the network and uses the three ways handshake model to establish the connection which makes it more reliable.


### 49. What is the UDP protocol?

UDP is the User Datagram Protocol and is based on Datagrams. Mainly, it is used for multicasting and broadcasting. Its functionality is almost the same as TCP/IP Protocol except for the three ways of handshaking and error checking. It uses a simple transmission without any hand-shaking which makes it less reliable.


### 50. Compare between TCP and UDP
| TCP/IP | 	UDP| 
|-|-|
| Connection-Oriented Protocol 	| Connectionless Protocol| 
| More Reliable | 	Less Reliable| 
| Slower Transmission 	| Faster Transmission| 
| Packets order can be preserved or can be rearranged 	| Packets order is not fixed and packets are independent of each other
| Uses three ways handshake model for connection|	No handshake for establishing the connection| 
| TCP packets are heavy-weight 	| UDP packets are light-weight| 
| Offers error checking mechanism | 	No error checking mechanism| 
| Protocols like HTTP, FTP, Telnet, SMTP, HTTPS, etc use TCP at the transport layer | 	Protocols like DNS, RIP, SNMP, RTP, BOOTP, TFTP, NIP, etc use UDP at the transport layer| 

### 51. What is the ICMP protocol?

ICMP is the Internet Control Message Protocol. It is a network layer protocol used for error handling. It is mainly used by network devices like routers for diagnosing the network connection issues and crucial for error reporting and testing if the data is reaching the preferred destination in time. It uses port 7 by default.


### 52. What do you mean by the DHCP Protocol?

DHCP is the Dynamic Host Configuration Protocol.

It is an application layer protocol used to auto-configure devices on IP networks enabling them to use the TCP and UDP-based protocols. The DHCP servers auto-assign the IPs and other network configurations to the devices individually which enables them to communicate over the IP network. It helps to get the subnet mask, IP address and helps to resolve the DNS. It uses port 67 by default.


### 53. What is the ARP protocol?

ARP is Address Resolution Protocol. It is a network-level protocol used to convert the logical address i.e. IP address to the device's physical address i.e. MAC address. It can also be used to get the MAC address of devices when they are trying to communicate over the local network.

### 54. What is the FTP protocol?

FTP is a File Transfer Protocol. It is an application layer protocol used to transfer files and data reliably and efficiently between hosts. It can also be used to download files from remote servers to your computer. It uses port 27 by default.


### 55. What is the MAC address and how is it related to NIC?

MAC address is the Media Access Control address. It is a 48-bit or 64-bit unique identifier of devices in the network. It is also called the physical address embedded with Network Interface Card (NIC) used at the Data Link Layer. NIC is a hardware component in the networking device using which a device can connect to the network.


### 56. Differentiate the MAC address with the IP address

The difference between MAC address and IP address are as follows:
|MAC Address |	IP Address|
|-|-|
|Media Access Control Address |	Internet Protocol Address|
|6 or 8-byte hexadecimal number |	4 (IPv4) or 16 (IPv6) Byte address|
|It is embedded with NIC |	It is obtained from the network|
|Physical Address |	Logical Address|
|Operates at Data Link Layer |	Operates at Network Layer.|
|Helps to identify the device |	Helps to identify the device connectivity on the network.|

### 57. What is a subnet?

A subnet is a network inside a network achieved by the process called subnetting which helps divide a network into subnets. It is used for getting a higher routing efficiency and enhances the security of the network. It reduces the time to extract the host address from the routing table.

### 58. Compare the hub vs switch
|Hub 	|Switch|
|-|-|
|Operates at Physical Layer |	Operates at Data Link Layer|
|Half-Duplex transmission mode 	|Full-Duplex transmission mode|
|Ethernet devices can be connectedsend 	|LAN devices can be connected|
|Less complex, less intelligent, and cheaper |	Intelligent and effective|
|No software support for the administration |	Administration software support is present|
|Less speed up to 100 MBPS 	|Supports high speed in GBPS|
|Less efficient as there is no way to avoid collisions when more than one nodes sends the packets at the same time |	More efficient as the collisions can be avoided or reduced as compared to Hub|

### 59. What is the difference between the ipconfig and the ifconfig?
|ipconfig |	ifconfig|
|-|-|
|Internet Protocol Configuration 	|Interface Configuration|
|Command used in Microsoft operating systems to view and configure network interfaces |	Command used in MAC, Linux, UNIX operating systems to view and configure network interfaces|

### 60.  What is the firewall?

The firewall is a network security system that is used to monitor the incoming and outgoing traffic and blocks the same based on the firewall security policies. It acts as a wall between the internet (public network) and the networking devices (a private network). It is either a hardware device, software program, or a combination of both. It adds a layer of security to the network.

### 61.  What are Unicasting, Anycasting, Multicasting and Broadcasting?

- **Unicasting:** If the message is sent to a single node from the source then it is known as unicasting. This is commonly used in networks to establish a new connection.
- **Anycasting:** If the message is sent to any of the nodes from the source then it is known as anycasting. It is mainly used to get the content from any of the servers in the Content Delivery System.
- **Multicasting:** If the message is sent to a subset of nodes from the source then it is known as multicasting. Used to send the same data to multiple receivers. 
- **Broadcasting:** If the message is sent to all the nodes in a network from a source then it is known as broadcasting. DHCP and ARP in the local network use broadcasting.



### 62. What happens when you enter google.com in the web browser?

Below are the steps that are being followed:

 - Check the browser cache first if the content is fresh and present in cache display the same.
 - If not, the browser checks if the IP of the URL is present in the cache (browser and OS) if not then request the OS to do a DNS lookup using UDP to get the corresponding IP address of the URL from the DNS server to establish a new TCP connection.
 - A new TCP connection is set between the browser and the server using three-way handshaking.
 - An HTTP request is sent to the server using the TCP connection.
 - The web servers running on the Servers handle the incoming HTTP request and send the HTTP response.
 - The browser process the HTTP response sent by the server and may close the TCP connection or reuse the same for future requests.
 - If the response data is cacheable then browsers cache the same.
 - Browser decodes the response and renders the content.


### 63. What causes latency

- **Physical distance:** the speed of light is the fastest anything can travel, so no matter how you design your system, transferring data through space will always take some time.
- **Complex computation:** if a computation is complex, it’s going to take longer to execute and increase latency. For example, a complex relational database query with lots of joins will take longer than a simple lookup by id. 
- **Congestion:** when there are many message requests coming in at once and the system doesn't have the capacity to process them all, some requests will have to wait, increasing latency. Either these requests will be dropped and sent again, or they'll sit in a queue waiting to be processed. 
- **Too many nodes:** if there are too many decision points in the pathway of a request, it will increase latency because each node along the way adds time while processing the request and deciding where to route it.


### 64. How to improve latency

- **Better paths:** minimizing the number of nodes a request has to travel through can help improve latencies. 
- **Caching:** caching can dramatically improve latencies when applied correctly, by storing a copy of repeatedly accessed data for faster retrieval.
- **Protocol choice** - certain protocols, like HTTP/2, intentionally reduce the amount of protocol overhead associated with a request, and can keep latency lower. TCP also has congestion avoidance features that can help mitigate congestion-related causes of high latencies.



### 65. What causes low throughput

- **Congestion** - just like road traffic is caused by many people trying to get to the same destination, low throughput in a software system can be caused by too many requests on the same network. Essentially, the hardware can't handle the number of requests going through it.
- **Protocol overhead** - if the protocols used in message transmission require handshakes and other back-and-forth communication patterns, the network can be overloaded with overhead from just the protocols and not the message content itself.
- **Latency** - since throughput is the amount of data transmitted over a set time period, high latencies (i.e. slow data transmission speeds) will reduce the amount of data that is transmitted overall.


### 66. How to improve throughput

- **Increasing bandwidth**- if you improve the capacity of a system to transport data (bandwidth), then the actual amount of data transferred (throughput) will increase too. This generally means adding new hardware or upgrading the hardware at bottlenecks in the system.
- **Improving latency**- since latency limits throughput, improving latency can improve throughput.
- **Protocol choice** - TCP has congestion avoidance features that can help mitigate congestion that causes low throughput.



### 67. What causes low availability

Downtime happens when part of the service breaks, like a hardware component fails, or a deployment goes wrong so the software is inconsistent. Systems can fail in many ways, and here are some of the most common:

- **Hardware failure** - computer components eventually fail, and this can take down a key server causing the whole system to stop working. A whole system can also be taken down if there’s a power outage or natural disaster at the data center.
- **Software bugs** - when something in the code is wrong, a request can run into a bug and the code can be killed (e.g. a null pointer is dereferenced)  
- **Complex architectures** - the more complex a system design is, the more points of failure there are, and the harder it gets to synchronize more computers and make them fault tolerant to other computers in the system failing. 
- **Dependent service outages** - an outage of a service that the system relies on, like DNS or an authorization server, can cause the system to become unavailable even if nothing is broken internally. 
- **Request overload** - if a system reaches its maximum capacity, it can start failing to respond to some requests. Too many requests can also cause the computer to shut down if it runs out of a key resource and can’t process any more operations (e.g. the disk space fills up).
- **Deployment issues** - when a deployment is conducted and the changes to software or configurations don’t go as expected, a number of problems can arise that could make the system unavailable. For example, deployment issues could put the servers in an inconsistent state, prevent them from starting, prevent them from talking to each other, or they might run short on resources. 


### 68. How to improve availability

The solution to partial system failure is redundancy - making sure that if something goes wrong there's a copy of it so the system can continue functioning. Redundancy has many components, including:

- **Failover systems** - duplicates of any part of the system that are switched to in the case of failure. These can be either hot failovers that run in parallel for immediate switch, or cold failovers that only start when needed.
- **Clustering** - running multiple instances of a part of the system, so if one node goes down the rest can manage without it.
- **Backups** - data backups and replication ensure that if the data storage fails, for example a power outage at the data center, there's another copy that can be accessed.
- **Geographic redundancy** - physically locating systems in different parts of the world, so if something happens that affects a region, there are redundant systems that still function. 
- **Automatic testing, deployment, and rollbacks** - to mitigate all the issues related to deploying new software or changing the architecture, it’s helpful to automate processes that catch software bugs, prevent human deployment errors, and automatically rollback to a previous stable deploy if something goes wrong. 



### 69. What are http status codes and name some
HTTP status codes that indicate what kind of response has been sent back. They are 3 digit codes that are grouped by the first number in the code. Each code has a corresponding “reason phrase” to make human interpretation easier.

    1XX - informational response e.g. `102 Processing`
    2XX - successful response e.g. `200 OK`
    3XX - redirection response e.g. `302 Found`
    4XX - client error response e.g. `404 Not Found`
    5XX - server error response e.g. `500 Internal Server Error`

### 70. What is a proxy
A proxy is a server that sits between a client and application server to provide some intermediary service to the communication. There are two kinds of proxies that provide different services: forward proxies and reverse proxies. 
### 71.  What is a forward proxy
A forward proxy sits between a pool of clients and the public internet. The goal of a forward proxy is to protect the particular client pool by filtering outgoing requests and incoming responses.

The common use cases for forward proxies are:

- Enforcing “terms of use” on a network
- Blocking malicious websites
- Anonymizing network traffic by using the IP address of the proxy instead of the client

### 72. What is reverse Proxies 
A reverse proxy sits between the public internet and a pool of servers. Because of their location in the system as an intermediary, reverse proxies can provide a number of services, including:

    Anonymizing the cluster servers
    SSL termination
    Load balancing
    Caching
    Filtering requests
    Attack prevention (e.g. DOS detection)


### 73. What is Load balancing?
Load balancing is the process of distributing tasks over a set of computing nodes to improve the performance and reliability of the system. A load balancer can be a hardware or software system, and it has implications for security, user sessions, and caching. 
There are two main types of Load Balancers (LB), their names referring to layers in the OSI model of network communication. L4 LBs operate at Layer 4, the transport layer, and L7 LBs operate at Layer 7, the application layer. 

There are many algorithms for deciding exactly how to distribute tasks. The most commonly used classes of algorithms are Round Robin, Least Load, and User and Resource Hashing. Some of these methods are only available on L7 LBs.
### 74. Advantages of load balancing


    Enable horizontal scaling: spinning up multiple instances of a service is not possible without a load balancer directing traffic efficiently to the cluster. 
    Dynamic scaling: it's possible to seamlessly add and remove servers to respond to load.
    Abstraction: the end user only needs to know the address of the load balancer, not the address of every server in the cluster.
    Throughput: service availability and response time are unaffected by overall traffic.
    Redundancy: distributing load over a cluster means no one server is a single point of failure. Note that the load balancer itself must also not become a single point of failure.
    Continuous deployment: it's possible to roll out software updates without taking the whole service down, by using the load balancer to take out one machine at a time.


### 75. Types of load balancers
2.1 Hardware vs software load balancers

- Hardware load balancers are specialized appliances with circuitry designed to perform load balancing tasks. They are generally very performant and very expensive. Hardware LBs are generally L4 LBs, because L7 decisions are more complex and need to be updated more often.

- The most well-known and respected software load balancers are HAProxy and nginx. Software load balancers like these run on standard servers and are less hardware optimized, but cheaper to set up and run. With a software load balancer, requests are simply routed to the load balancer server instead of an application server. 
 



### 76. DNS vs L4 vs L7 load balancers
DNS load-balancers integrate with the Domain Name Services (DNS) infrastructure to cause a client’s name lookup for a service (e.g., for “www.google.com”) to return a different IP address to each requester corresponding to one of a pool of back-end servers in their geographic location.

### 77. Load balancing algorithms

Load balancing algorithms are generally divided into two groups: static and dynamic. Static algorithms function the same regardless of the state of the back end serving the requests, whereas dynamic algorithms take into account the state of the backend and consider system load when routing requests.

- Static

    - Round robin is the simplest and one of the most used algorithms. The load balancer maintains a list of available servers, and routes the first request to the first server, the second request to the second server, and so on. This works well if every server in the pool has roughly the same performance characteristics. A “weighted” round robin takes server characteristics into account, so that servers with more resources get proportionally more of the requests. The advantages of this algorithm are that it is simple, very fast, and easy to understand. The disadvantages are that the current load of each server is not taken into account, and that the relative computation cost of each request is also not taken into account.

    - A Random algorithm is another simple and popular approach. Requests are sent to random servers, which can be weighted by server capacity. Random works well for systems with a large number of requests because the law of large numbers means randomization will tend towards a uniform distribution. It also works well with running several LBs at the same time, because they don’t need to coordinate. 
- Dynamic

    - Least Load algorithm, requests are sent to the server with the lowest load at the time of request. Load can be measured with a variety of metrics, including number of connections, amount of traffic, and request latency. 
    - “power-of-d-choices” algorithm is popular for large distributed clusters because it effectively addresses a problem that arises when we have a pool of independent load balancers instead of a single load balancer. If every LB in the pool sends a request to the least busy server, then that server will be hit with requests from all LBs and quickly become overloaded. 

### 78. Load balancers and security

Since L7 LBs need to examine the request to make routing decisions, any encrypted requests (HTTPS) need to be decrypted. That means an L7 LB will terminate the TCP connection with the request source and start a new connection to pass the request to the backend servers. This new request can be encrypted or not, depending how much you trust your backend server network.

Load Balancers are also a natural point of protection against DDOS attacks. Since they generally prevent server overload by distributing requests well, in the case of a DDOS attack the LB makes it harder to overload the whole system. They also remove a single point of failure, and therefore make the system harder to attack

### 79. Leader election
A leader election algorithm describes how a cluster of nodes without a leader can communicate with each other to choose exactly one of themselves to become the leader. The algorithm is executed whenever the cluster starts or when the leader node goes down. 
### 80. When to use Leader election 

There are three cases to consider when deciding if leader election fits the situation.

- The first case is when each node is roughly the same and there isn't a clear candidate for a permanently assigned leader. This means any node can be elected as leader, and there isn’t a single point of failure required to coordinate the system.

- The second case is when the cluster is doing particularly complex work that needs good coordination. Coordination can mean anything from decisions about how the work is to be divided, to assigning work to specific nodes, or to synthesizing the results of work from different nodes.

- The third case where leader election adds value is when a system executes many distributed writes to data and requires strong consistency. You can read more about consistency in our article on Databases, but essentially this means it's very important that no matter what node handles a request the user will always have the most up-to-date version of the data. In this situation a leader creates consistency guarantees by being the source of truth on what the most recent state of the system is (and the leader election algorithm must preserve this properly). 
### 81. Drawbacks of leader election

The main downside to leader election is complexity: a bad implementation can end up with “split brain” where two leaders try to control at the same time, or no leader is elected and the cluster can’t coordinate. As such, leader election should only be used when there is a need for complex coordination or strong consistency, and none of the alternatives fit the situation.

### 82. Leader Election Algorithms
A leader election algorithm guides a cluster to collectively agree on one node to act as leader with as few back and forth communications as possible.

Generally, the algorithm works by assigning one of three states to each node: Leader, Follower, or Candidate. Additionally the leader will be required to regularly pass a "healthcheck" or “heartbeat” so follower nodes can tell if the leader has become unavailable or failed and a new one needs to be elected.

The kind of leader election algorithm you want depends on whether the cluster is synchronous or asynchronous. In a synchronous cluster nodes are synchronized to the same clock and send messages in predictable amounts of time and ordering. In an asynchronous cluster messages are not reliably delivered within a certain amount of time or in any order. 

- **Bully Algorithm:** The Bully Algorithm is a simple synchronous leader election algorithm. This algorithm requires that each nodes has a unique numeric id, and that nodes know the ids of all other nodes in the cluster.
The election process starts when a node starts up or when the current leader fails the healthcheck. There are two cases:

  - if the node has the highest id, it declares itself the winner and sends this message to the rest of the nodes.
  - if the node has a lower id, it messages all nodes with higher ids and if it doesn't get a response, it assumes all of them have failed or are unavailable, and declares itself the winner.

- **Paxos** is a general consensus protocol that can be used for asynchronous leader election. Quite a lot of research has been done about the Paxos family of algorithms, which means it's both robust and there's much more to say about it than we have space for in this article.
- **RAFT** is an alternative to Paxos that is favored because people tend to find it simpler to understand, and therefore easier to implement and use. Raft is an asynchronous algorithm.
In Raft consensus, each node keeps track of the current "election term". When leader election starts each node increments its copy of the term number and listens for messages from other nodes. After a random interval, if the node doesn't hear anything, it will become a candidate leader and ask other nodes for votes. 

- **Apache ZooKeeper (ZAB)** Apache Zookeeper is a centralized coordination service that is “itself distributed and highly reliable.” The ethos behind Apache ZooKeeper is that coordination in distributed systems is difficult, and it’s better to have a shared open source implementation with all the key elements so that your service doesn’t have to reimplement everything from scratch. This is especially helpful in large distributed systems.
### 83. Alternatives to leader election

Alternatives to leader election are based on the premise that coordination is possible without a dedicated leader node, thus achieving the primary function of leader election with lower implementation complexity. 
- **Locking:** A locking model ensures that concurrent operations on a shared resource don't conflict by only allowing changes from one node at a time. With optimistic locking a node will read a resource and its version id, make changes, and then before updating make sure that the version id is the same. If the id is different this means the resource has been updated since the node first read it. Going forward with the intended changes based on the old id would lose the other changes, so  the node needs to try again. In pessimistic locking a node locks the resource, makes changes, and then unlocks the resource. 
- **Idempotent APIs:** APIs can have the feature of idempotency to ensure consistent interactions with a shared resource. An API is idempotent when the same request sent multiple times will not produce any inconsistent results. When reading from a resource, this means the response will always be the same value. When writing, this means the update will only happen once.

- **Workflow Engines:** Another way of coordinating nodes in a system is by using a workflow engine . A workflow engine is a centralized decision making system that contains a set of "workflows" of what work can be done, the state of data and work in the system, and the resources available to assign work to. Popular solutions are AWS Step Functions, Apache Airflow, and .NET State Machines

### 84. Purpose of polling, SSE, and WebSockets

The internet is built on the HTTP standard for communicating data between web browsers and web servers. The client, in most cases a web browser, makes an HTTP request to the server, which sends back the appropriate response. This roundtrip is what happens when you type an address like 'http://www.example.com' into your browser, and you get a web page back.
The HTTP standard is widely supported and very functional. But when your application needs to transmit continuous information streams or real-time updates to clients, like a collaborative document editor that shows changes in real time. In cases like this, having to repeatedly make regular HTTP requests will slow things down.

That’s where polling, WebSockets, and SSE come in. These are three protocols that specifically focus on speed and memory efficiency for data streams. Which approach you’d want to use in a system depends on the use case. So, let’s  go over how each of these protocols work, and when to use them.

### 85. Short Polling

Short polling is the original polling protocol for clients to get regular information updates from a server. The steps of short polling are:

- Client sends Server an HTTP request for new information.
- Server responds with new information, or no information.
- Client repeats the request at a set interval (e.g. 2s)




### 86. Long Polling

Long polling is a more efficient version of short polling. The steps of long polling are:
Long polling cuts down the number of HTTP requests necessary to transmit the same amount of data to the client. The server has to be able to “hold” unfulfilled client requests, and handle the case where it gets new information to send, but the client hasn’t sent a new request yet. 
- Client sends Server and HTTP request for new information
- Server waits until there’s new information to respond (a “hanging” response)
- Client repeats the request as soon as it gets the previous response back


### 87. Server Sent Events

Server Sent Events provide a one-way connection for a server to push new data to a client, without reestablishing a connection every time. For example a social media app could use SSE to push new posts to a user feed as soon as they’re available. SSE connections follow the EventSource interface, which uses HTTP to make the underlying communications.

At a high level, the steps of SSE are:

  - Client creates a new EventSource object targeting the server
  - Server registers SSE connection
  - Server sends new data to the client
  - Client receives messages with EventSource handlers
  - Either side closes the connection


### 88. WebSockets

WebSockets is a two-way message passing protocol based on TCP (the protocol at Layer 4 of the OSI networking model). WebSockets are faster for data transmission than HTTP because it has less protocol overhead and operates at a lower level in the network stack. At a high level, the steps of a websocket connection are:

    Client and Server establish a connection over HTTP and then “upgraded” using the WebSockets handshake
    WebSockets TCP messages are transmitted in both directions over port 443 (or 80 if it’s not TLS encrypted) 
    Either side closes the connection


### 89. Why use WebSocket over HTTP?
A WebSocket is a continuous connection between client and server. That continuous connection allows the following:

- Data can be sent from server to client at any time, without the client even requesting it. This is often called server-push and is very valuable for applications where the client needs to know fairly quickly when something happens on the server (like a new chat messages has been received or a new price has been udpated). A client cannot be pushed data over http. The client would have to regularly poll by making an http request every few seconds in order to get timely new data. Client polling is not efficient.

- Data can be sent either way very efficiently. Because the connection is already established and a webSocket data frame is very efficiently organized, one can send data a lot more efficiently that via an HTTP request that necessarily contains headers, cookies, etc...
### 90. Mention some advantages of SSE over WebSockets
- Transported over simple HTTP instead of a custom protocol
- Can be poly-filled with javascript to "backport" SSE to browsers that do not support it yet.
- Built in support for re-connection and event-id
- Simpler protocol
- No trouble with corporate firewalls doing packet inspection
### 91. What is Pub/Sub?

Pub/Sub stands for “publish/subscribe.” It is a messaging pattern that allows for loose coupling between applications. With Pub/Sub, applications can subscribe to certain topics, and then receive messages only for those topics. This allows for a more flexible architecture, as applications can come and go without affecting the overall system.

### 92. Can you explain the basic concepts and components of a publish-subscribe system?

In a publish-subscribe system, there are three main components: publishers, subscribers, and a broker. Publishers are the ones who generate the content that is to be shared, subscribers are the ones who want to receive that content, and the broker is the one who manages the distribution of the content. 

### 93. What are some common use cases for Pub/Sub systems?

Some common use cases for Pub/Sub systems include social media applications, chat applications, and gaming applications.

### 94.  How does Pub/Sub differ from traditional request-response approaches to communication?

In a traditional request-response approach, a client sends a request to a server and then waits for a response. With Pub/Sub, the client subscribes to a topic and then receives messages as they are published, without having to send a request. This can be useful when you want to receive updates in real-time, without having to constantly send requests.

### 95. Is it possible for multiple subscribers to receive messages published by a single publisher in Pub/Sub? If yes, then how do publishers control who receives their message?

Yes, it is possible for multiple subscribers to receive messages published by a single publisher in Pub/Sub. Publishers can control who receives their message by specifying the topic that the message should be published to. Subscribers can then subscribe to the appropriate topic in order to receive the message.

### 96. What’s your opinion on using Pub/Sub when there are only two parties involved?

I believe that Pub/Sub can be beneficial even when there are only two parties involved. It can help to decouple the components of your system and make it easier to scale. Additionally, it can help to improve performance by reducing the number of dependencies between components.

### 97. Why would anyone choose Polling over Event-Driven Pub/Sub Systems?

Polling is a simple and straightforward way to check for new data. It can be easily implemented and does not require a lot of infrastructure. Event-driven pub/sub systems are more complex and can be more difficult to set up and maintain. However, they are more efficient and can scale better to handle large amounts of data.

### 98. What are some advantages of Pub/Sub over other architectural styles like RPC or REST?

Pub/Sub has a few advantages over other architectural styles. First, it allows for decoupling of components, so that components can communicate without needing to know about each other. Second, it can improve performance by reducing the number of messages that need to be sent. Finally, it can provide a more scalable solution since messages can be sent to multiple subscribers at once.

### 99. What is an event bus?

An event bus is a software architecture pattern that allows for loose coupling between software components by providing a central place for them to communicate. This communication is typically in the form of events, which can be emitted by one component and then received and handled by another. Event buses can be used to decouple components in a variety of different ways, making them very flexible.

### 100. What is the difference between topics and queues in Pub/Sub?

Topics are used for one-to-many communication, where messages are broadcast to all subscribers of the topic. Queues are used for one-to-one communication, where each message is delivered to a single subscriber.

### 101. What happens if no subscriber is available at the time of publishing?

If there are no subscribers available when a message is published, then the message will be lost.


### 102. Can you give me some examples of use cases where a Pub/Sub architecture works well?

Pub/Sub is a great way to handle communication between different parts of a system where there are a lot of messages being sent and received. It can be used for things like chat applications, news feeds, or any other system where there are a lot of messages being exchanged.

### 103. Can you explain what asynchronous messaging is?

Asynchronous messaging is a method of communication between two or more parties in which the messages are not sent or received at the same time. This type of messaging can be useful when the parties are not able to communicate in real-time, or when the message sender does not need an immediate response from the message receiver.

### 104. What is the difference between synchronous and asychronous messaging models?

The synchronous messaging model is a one-to-one model where each message is sent from one sender to one receiver. The asynchronous messaging model is a one-to-many model where each message can be sent to multiple receivers.

### 105. What happens if a message fails to be delivered to one of its intended recipients?

If a message fails to be delivered to one of its intended recipients, then it will be placed in a dead letter queue. The message will remain in the dead letter queue until it is either delivered to the intended recipient or it expires.

### 106. What are durable and non-durable subscriptions?

A durable subscription is one where the messages are stored by the message broker until they are consumed, even if the consumer is not active at the time the message is published. A non-durable subscription is one where messages are only stored until they are consumed or until the message broker restarts, at which point they are lost.

### 107. Can you explain what dequeuing means in context with Pub/Sub?

Dequeuing is the process of removing messages from a queue. In the context of Pub/Sub, this would refer to removing messages from the message queue that have been published by the publisher and are awaiting processing by the subscriber.

### 108. What is Pub/Sub used for in cloud computing scenarios?

Pub/Sub is a messaging pattern that is often used in cloud computing scenarios. It allows for communication between different parts of a system, or between different systems, in a decoupled way. This means that each part of the system can subscribe to the messages that it is interested in, and does not need to be aware of the other parts of the system.

### 109.  How can you ensure that messages published through Pub/Sub are received by all subscribers?

There are a few ways to ensure that messages published through Pub/Sub are received by all subscribers. One way is to use a message queue, which will hold onto messages until all subscribers have received them. Another way is to use a fan-out exchange, which will send a copy of the message to all subscribers.

### 110. What are Message queues

Message queues are a kind of messaging-oriented middleware where producers push new messages to a named First-In, First-Out (FIFO) queue, which consumers can then pull from.

Message queues are also called point-to-point messaging because there is a one-to-one relationship between a message’s producer and consumer. There can be many producers and consumers using the same queue, but any particular message will only have one producer and one consumer. 

### 111. What do you understand by RESTful Web Services?

RESTful web services are services that follow REST architecture. REST stands for Representational State Transfer and uses HTTP protocol (web protocol) for implementation. These services are lightweight, provide maintainability, scalability, support communication among multiple applications that are developed using different programming languages. They provide means of accessing resources present at server required for the client via the web browser by means of request headers, request body, response body, status codes, etc.


### 112. What is a REST Resource?

Every content in the REST architecture is considered a resource. The resource is analogous to the object in the object-oriented programming world. They can either be represented as text files, HTML pages, images, or any other dynamic data.

    The REST Server provides access to these resources whereas the REST client consumes (accesses and modifies) these resources. Every resource is identified globally by means of a URI.



### 113. What is URI?

Uniform Resource Identifier is the full form of URI which is used for identifying each resource of the REST architecture. URI is of the format:

<protocol>://<service-name>/<ResourceType>/<ResourceID>




### 114. Types of URI

There are 2 types of URI:

    URN: Uniform Resource Name identifies the resource by means of a name that is both unique and persistent.
        URN doesn’t always specify where to locate the resource on the internet. They are used as templates that are used by other parsers to identify the resource.
        These follow the urn scheme and usually prefixed with urn:. Examples include
            urn:isbn:1234567890 is used for identification of book based on the ISBN number in a library application.
            urn:mpeg:mpeg7:schema:2001 is the default namespace rules for metadata of MPEG-7 video.
        Whenever a URN identifies a document, they are easily translated into a URL by using “resolver” after which the document can be downloaded.
    URL: Uniform Resource Locator has the information regarding fetching of a resource from its location.
        Examples include:
            http://abc.com/samplePage.html
            ftp://sampleServer.com/sampleFile.zip
            file:///home/interviewbit/sampleFile.txt
        URLs start with a protocol (like ftp, http etc) and they have the information of the network hostname (sampleServer.com) and the path to the document(/samplePage.html). It can also have query parameters.

### 115. What are the features of RESTful Web Services?

Every RESTful web service has the following features:

    The service is based on the Client-Server model.
    The service uses HTTP Protocol for fetching data/resources, query execution, or any other functions.
    The medium of communication between the client and server is called “Messaging”.
    Resources are accessible to the service by means of URIs.
    It follows the statelessness concept where the client request and response are not dependent on others and thereby provides total assurance of getting the required data.
    These services also use the concept of caching to minimize the server calls for the same type of repeated requests.
    These services can also use SOAP services as implementation protocol to REST architectural pattern.



### 116. What is the concept of statelessness in REST?

The REST architecture is designed in such a way that the client state is not maintained on the server. This is known as statelessness. The context is provided by the client to the server using which the server processes the client’s request. The session on the server is identified by the session identifier sent by the client.

### 117. What do you understand by JAX-RS?

As the name itself stands (JAX-RS= Java API for RESTful Web Services) is a Java-based specification defined by JEE for the implementation of RESTful services. The JAX-RS library makes usage of annotations from Java 5 onwards to simplify the process of web services development. The latest version is 3.0 which was released in June 2020. This specification also provides necessary support to create REST clients.


### 118. What are the HTTP Methods?

HTTP Methods are also known as HTTP Verbs. They form a major portion of uniform interface restriction followed by the REST that specifies what action has to be followed to get the requested resource. Below are some examples of HTTP Methods:

    GET: This is used for fetching details from the server and is basically a read-only operation.
    POST: This method is used for the creation of new resources on the server.
    PUT: This method is used to update the old/existing resource on the server or to replace the resource.
    DELETE: This method is used to delete the resource on the server.
    PATCH: This is used for modifying the resource on the server.
    OPTIONS: This fetches the list of supported options of resources present on the server.

The POST, GET, PUT, DELETE corresponds to the create, read, update, delete operations which are most commonly called CRUD Operations.

### 119. Can you tell the disadvantages of RESTful web services?

The disadvantages are:

    As the services follow the idea of statelessness, it is not possible to maintain sessions. (Session simulation responsibility lies on the client-side to pass the session id)
    REST does not impose security restrictions inherently. It inherits the security measures of the protocols implementing it. Hence, care must be chosen to implement security measures like integrating SSL/TLS based authentications, etc.



### 120. Define Messaging in terms of RESTful web services.

The technique of sending a message from the REST client to the REST server in the form of an HTTP request and the server responding back with the response as HTTP Response is called Messaging. The messages contained constitute the data and the metadata about the message.

### 121. While creating URI for web services, what are the best practices that needs to be followed?

Below is the list of best practices that need to be considered with designing URI for web services:

    While defining resources, use plural nouns. Example: To identify user resource, use the name “users” for that resource.
    While using the long name for resources, use underscore or hyphen. Avoid using spaces between words. For example, to define authorized users resource, the name can be “authorized_users” or “authorized-users”.
    The URI is case-insensitive, but as part of best practice, it is recommended to use lower case only.
    While developing URI, the backward compatibility must be maintained once it gets published. When the URI is updated, the older URI must be redirected to the new one using the HTTP status code 300.
    Use appropriate HTTP methods like GET, PUT, DELETE, PATCH, etc. It is not needed or recommended to use these method names in the URI. Example: To get user details of a particular ID, use /users/{id} instead of /getUser
    Use the technique of forward slashing to indicate the hierarchy between the resources and the collections. Example: To get the address of the user of a particular id, we can use: /users/{id}/address



### 122. What are the best practices to develop RESTful web services?

RESTful web services use REST API as means of implementation using the HTTP protocol. REST API is nothing but an application programming interface that follows REST architectural constraints such as statelessness, cacheability, maintainability, and scalability. It has become very popular among the developer community due to its simplicity. 

### 123. Can you tell what constitutes the core components of HTTP Request?

In REST, any HTTP Request has 5 main components, they are:

    Method/Verb − This part tells what methods the request operation represents. Methods like GET, PUT, POST, DELETE, etc are some examples.
    URI − This part is used for uniquely identifying the resources on the server.
    HTTP Version − This part indicates what version of HTTP protocol you are using. An example can be HTTP v1.1.
    Request Header − This part has the details of the request metadata such as client type, the content format supported, message format, cache settings, etc.
    Request Body − This part represents the actual message content to be sent to the server.


### 124. What constitutes the core components of HTTP Response?

HTTP Response has 4 components:

    Response Status Code − This represents the server response status code for the requested resource. Example- 400 represents a client-side error, 200 represents a successful response.
    HTTP Version − Indicates the HTTP protocol version.
    Response Header − This part has the metadata of the response message. Data can describe what is the content length, content type, response date, what is server type, etc.
    Response Body − This part contains what is the actual resource/message returned from the server.


### 125.  Define Addressing in terms of RESTful Web Services.

Addressing is the process of locating a single/multiple resources that are present on the server. This task is accomplished by making use of URI (Uniform Resource Identifier). The general format of URI is 

<protocol>://<application-name>/<type-of-resource>/<id-of-resource>



### 126. What makes REST services to be easily scalable?

REST services follow the concept of statelessness which essentially means no storing of any data across the requests on the server. This makes it easier to scale horizontally because the servers need not communicate much with each other while serving requests.


### 127. Based on what factors, you can decide which type of web services you need to use - SOAP or REST?

REST services have gained popularity due to the nature of simplicity, scalability, faster speed, improved performance, and multiple data format support. But, SOAP has its own advantages too. Developers use SOAP where the services require advanced security and reliability.

Following are the questions you need to ask to help you decide which service can be used:

    Do you want to expose resource data or business logic?
        SOAP is commonly used for exposing business logic and REST for exposing data.
    Does the client require a formal strict contract?
        If yes, SOAP provides strict contracts by using WSDL. Hence, SOAP is preferred here.
    Does your service require support for multiple formats of data?
        If yes, REST supports multiple data formats which is why it is preferred in this case.
    Does your service require AJAX call support?
        If yes, REST can be used as it provides the XMLHttpRequest.
    Does your service require both synchronous and asynchronous requests?
        SOAP has support for both sync/async operations.
        REST only supports synchronous calls.
    Does your service require statelessness?
        If yes, REST is suitable. If no, SOAP is preferred.
    Does your service require a high-security level?
        If yes, SOAP is preferred. REST inherits the security property based on the underlying implementation of the protocol. Hence, it can’t be preferred at all times.
    Does your service require support for transactions?
        If yes, SOAP is preferred as it is good in providing advanced support for transaction management.
    What is the bandwidth/resource required?
        SOAP involves a lot of overhead while sending and receiving XML data, hence it consumes a lot of bandwidth.
        REST makes use of less bandwidth for data transmission.
    Do you want services that are easy to develop, test, and maintain frequently?
        REST is known for simplicity, hence it is preferred.



### 128. Can we implement transport layer security (TLS) in REST?

Yes, we can. TLS does the task of encrypting the communication between the REST client and the server and provides the means to authenticate the server to the client. It is used for secure communication as it is the successor of the Secure Socket Layer (SSL). HTTPS works well with both TLS and SSL thereby making it effective while implementing RESTful web services. One point to mention here is, the REST inherits the property of the protocol it implements. So security measures are dependent on the protocol REST implements.


### 129. Should we make the resources thread safe explicitly if they are made to share across multiple clients?

There is no need to explicitly making the resources thread-safe because, upon every request, new resource instances are created which makes them thread-safe by default.


### 130. What is Payload in terms of RESTful web services?

Payload refers to the data passes in the request body. It is not the same as the request parameters. The payload can be sent only in POST methods as part of the request body.


### 131. Is it possible to send payload in the GET and DELETE methods?

No, the payload is not the same as the request parameters. Hence, it is not possible to send payload data in these methods.


### 132. How can you test RESTful Web Services?

RESTful web services can be tested using various tools like Postman, Swagger, etc. Postman provides a lot of features like sending requests to endpoints and show the response which can be converted to JSON or XML and also provides features to inspect request parameters like headers, query parameters, and also the response headers. Swagger also provides similar features like Postman and it provides the facility of documentation of the endpoints too. We can also use tools like Jmeter for performance and load testing of APIs.


### 133. What is the maximum payload size that can be sent in POST methods?

Theoretically, there is no restriction on the size of the payload that can be sent. But one must remember that the greater the size of the payload, the larger would be the bandwidth consumption and time taken to process the request that can impact the server performance.


### 134. How does HTTP Basic Authentication work?

While implementing Basic Authentication as part of APIs, the user must provide the username and password which is then concatenated by the browser in the form of “username: password” and then perform base64 encoding on it. The encoded value is then sent as the value for the “Authorization” header on every HTTP request from the browser. Since the credentials are only encoded, it is advised to use this form when requests are sent over HTTPS as they are not secure and can be intercepted by anyone if secure protocols are not used.


### 135. What is the difference between idempotent and safe HTTP methods?

    Safe methods are those that do not change any resources internally. These methods can be cached and can be retrieved without any effects on the resource.
    Idempotent methods are those methods that do not change the responses to the resources externally. They can be called multiple times without any change in the responses.


### 136. What are the key features provided by JAX-RS API in Java EE?

JAX-RS stands for Java API for RESTful Web services. They are nothing but a set of Java-based APIs that are provided in the Java EE which is useful in the implementation and development of RESTful web services.

Features of JAX-RS are:

    POJO-based: The APIs in the JAX-RS is based on a certain set of annotations, classes, and interfaces that are used with POJO (Plain Old Java Object) to expose the services as web services.
    HTTP-based: The JAX-RS APIs are designed using HTTP as their base protocol. They support the HTTP usage patterns and they provide the corresponding mapping between the HTTP actions and the API classes.
    Format Independent: They can be used to work with a wide range of data types that are supported by the HTTP body content.
    Container Independent: The APIs can be deployed in the Java EE container or a servlet container such as Tomcat or they can also be plugged into JAX-WS (Java API for XML-based web services) providers.



### 137. Describe Ajax.
Asynchronous JavaScript and XML (AJAX) is a technique that uses XMLHttpRequest objects to update web pages asynchronously by exchanging a small amount of data with the server, update the page without page reload. It is a front-end tool that communicates with the back-end server from the browser.
### 138. List Ajax features.

    High performing web pages and user-friendly features like autocomplete suggestions
    Help in Template rendering at the client-side
    Client component declarative instantiation
    Use of Observer pattern on JavaScript arrays and objects
    Invoke ADO.Net data contexts and services
    Assists in Data View control and binding live data

### 139. List advantages of using Ajax in web development

    Ajax reduces latency-response time in both Request/Response.
    XMLHttpRequest object in Ajax is highly responsive in data transfer in specific areas without page reload.
    Asynchronous calls to Server prevent client’s wait for data before rendering.
    Form validation is instant using Ajax.
    Bandwidth use is reduced when Ajax is used in fetching and storing data from the database in the background without page reload.

### 140.  What are the limitations of Ajax?

    Ajax is not advisable in developing web applications but is great for websites.
    View page source display code is written in Ajax exposing the functionality.
    It is complex, less secured, needs more time in developing web pages.
    Search engines cannot index pages developed using Ajax as Crawlers cannot identify web applications developed in JavaScript and Ajax.
    XMLHttpRequest object can only fetch information from the server where pages are hosted but cannot fetch information from another server.
    It is not possible to bookmark pages developed in Ajax.
    Ajax cannot function with JavaScript disabled in the browser.
    It has a slow response time because different page controls load at different times.
    Dynamic page registration of its own on browser history engine is not possible, the code-behind file function does not work.

### 141. List Ajax frameworks.

    JavaScript frameworks like jQuery, MooTools, Prototype, YUI library, Dojo, AngularJS, Webix, GWT (Google Web Toolkit)
    Java frameworks like Apache Wicket, JSF (Java Server Faces), RichFaces, ICEfaces, PrimeFaces
    Windows .NET platform offers ASP.NET AJAX
    Python framework such as Pyjs.
    Ruby framework like Ruby on Rails

### 142. Explain the working of Ajax.
Ajax with XMLHttpRequest object communicates with a server, renders data on a portion of a webpage without page reload.

List of steps that take place while working at Ajax are:

    The user request is sent to the server from the browser.
    JavaScript calls XMLHttpRequest object.
    The server interacts with the database using ASP.Net, JSP, or PHP.
    Data is fetched.
    XMLHttpRequest callback receives XML or JSON data from server.
    The browser displays HTML and CSS data on a particular portion of the page without page reload.

### 143. What are the security threats that prevail with Ajax code?

    Ajax request calls are in plain text format, resulting in insecure access to the database.
    Data retrieved gets stored on the client browser so anyone can view it.
    It makes monitoring browser sessions with help of a script.
    Entire Ajax code can be seen using view page source, hackers can misuse this code in a cyber attack.

### 144. What is XMLHttpRequest?

XMLHttpRequest is an API that has methods and properties used by various scripting languages such as JavaScript, VBScript for manipulating and transferring XML data using HTTP protocol connecting client and server.

Various formats supported by XMLHttpRequest for data transfer are XML, JSON, plain text, and even binary content. XMLHttpRequest object help update parts of the webpage without reloading the page. It recognizes events that occur during the processing of the request.

### 145. List various properties of XMLHttpRequest.

    onreadystatechange – For every state changes event gets fired by event handler.
    readyState – Defines current state of XMLHttpRequest
    responseText – Response is returned as string.
    responseXML – Response is returned as XML in XML document object and parsed using DOM tree properties and methods.
    status – status is returned as number. Example: 404 for “Not Found” 200 for “OK”
    statusText – status is returned as text. Example: “Not Found” or “OK”

### 146. Describe various methods used in XMLHttpRequest

    abort() – Used to cancel current request.
    getAllResponseHeaders() – Set of all the HTTP headers are returned as a string.
    getResponseHeader(header_name) – Returns specific HTTP header value.
    open(method,URL) – Various HTTP parameters such as GET, POST, HEAD, PUT and DELETE can be used as method. URL is the location of page on server where request should be sent.
    send(content) – Used to send the request to the server.
    setRequestHeader(label, value) – label-value pair is added to HTTP header to be sent.

### 147. Explain various ways open() method can be used for XMLHttpRequest.
Open() method of XMLHttpRequest object help to initialize new request or existing request. The parameters it uses contains request method, URL and other optional attributes.

    open ( method, URL )
    The value for the method parameter can be “GET”, “POST”, or “HEAD”. “PUT” and “DELETE” are some methods used in RESTful requests.
    URL is the string that has the path of HTTP server path for sending a request.
    open (method, URL, async)
    async – specifies if the request send should be handled asynchronously or not at the server. If the value of async is true, it means that after send() method the script processing should not wait for a response, false will mean the script will wait for a response before continuing for script process.
    open (method, URL, async, userName)
    username is optional for authentication. Its default value is null.
    open (method, URL, async, userName, password)
    password is optional for authentication. Its default value is null.

### 148. Explain Ajax callback function.

    Client browser sends a request message to Server.
    The user is free to do anything other than waiting for the response as the request call is asynchronous in nature.
    The server receives the message and processes the page for which Ajax callback is called.
    The response is sent to the browser as a JavaScript code string that gets executed in the browser.

### 149. List the steps to improve Ajax performance

    Limiting Ajax requests to a minimum
    A wise selection of events that triggers Ajax request
    Optimum use of GET request
    Minimize data amount transmission
    Use Caching to secure data




### 1. How would you design a social media app?
For this question you'll typically be asked to design a specific app, such as Twitter, Instagram, etc. For this example, we’ll assume the interviewer asked you to design Twitter. Here are some considerations for answering this question: 

Ask clarifying questions

    Is the interviewer looking for a design of the core features, or a high-level overview of the whole service?
    What are the constraints of the system?
    What are your assumptions? (traffic distribution, number of active users and tweets, read vs write-heavy)

Design high-level

    Back-of-the-envelope calculations: average KBs per tweet, size of new tweet content per month, read requests and tweets per second, etc.
    High-level components: write, read, and search APIs; types of databases; SQL vs NoSQL; etc

Drill down on your design

    Potential bottlenecks: adding a load balancer with multiple web servers, scalability issues, fanout service slowing down tweets and @replies, etc.
    Components that you could dive into: how a user views the home timeline or posts a tweet, the intricacies of the database design, etc.

Bring it all together

    Consider: does the final design address the bottlenecks you’ve identified? Does it meet the goals you discussed at the beginning of the interview? Do you have any questions for the interviewer?


### 2.  How would you design X game?

Another topic that comes up frequently is designing a classic game. The exact game you’ll be asked about varies, but here are some of the most common ones we’ve seen:

    Tic-tac-toe
    Chess
    Boggle
    Minesweeper
    Cards/poker

Let’s walk through an example of how you could approach the problem if you were asked to design a chess game. 

Ask clarifying questions

    What are the rules of the game? 
    How many players are there? Are there spectators?
    Do we need a timer? Are any other special functions required?

Design high-level

    Possible classes for the game:  board, piece, spot, etc.
    Methods that will be required for things like moving pieces

Drill down on your design

    Identify important attributes for each class, such as the grid coordinates and color of each spot
    Define how the game will prevent illegal moves and recognize a victory

Bring it all together

    Sense check your design, and confirm whether it has met all of the requirements you identified at the beginning of the interview



### 3. How would you design a parking lot?

For questions like these, interviewers are testing your skills in object-oriented design, to see whether you can apply technical thinking to physical objects. 

Ask clarifying questions

    Is this a multiple floor parking garage or a single level parking lot?
    How many entry and exit points will be needed, and for what types of vehicles?
    Are there monetary goals for this parking lot?

Design high-level

    Possible use cases: customers parking and paying for their spot, admin managing the system, parking attendants maintaining the lot and helping customers, etc.
    Possible classes of the system: ParkingLot, ParkingFloor, Account, ParkingTicket, Vehicle, etc.

Drill down on your design

    How will you diagram specific activities? (e.g. customers paying for parking tickets, display panels showing available spots, etc.)
    What are the required enums, data types, and constants of the eventual code for the parking lot system?

Bring it all together

    Will this system meet the requirements you’ve laid out with the interviewer in the beginning of the session?

For a full answer to this question, take a look at this text guide from Educative.io. You may also find this video walk-through from Think Software useful: 

### 4. How would you design a URL-shortening service?

URL shortening services like TinyURL, Bitly, etc. provide short link aliases that redirect to longer URLs. Here are some points of consideration to help you work out how to build this kind of system. 

Ask clarifying questions

    Will users be able to customize the URL?
    How long do the URLs last before they expire?
    What are the availability and latency requirements for this system?

Design high-level

    Back-of-the-envelope calculations: estimate the traffic and storage needs per month, as well as bandwidth and memory requirements
    Define the APIs (SOAP, REST, etc) as well as a general database schema (URL mappings and user data)

Drill down on your design

    Consider tradeoffs: encoding actual URLs may turn out the same shortened URL for two different users who enter the same URL. System may not work for URLs with URL-encoding. Concurrency may cause problems, etc.
    Where will you place load balancers, and how will you cache URLs?

Bring it all together

    Is the system you’ve designed highly available, so that URLs will not break if the servers go down? Does it meet any potential business objectives laid out at the start of the interview?


