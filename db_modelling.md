### 1. What is a Data Model?
A data model organizes different data elements and standardizes how they relate to one another and real-world entity properties. So logically then, data modeling is the process of creating those data models.
Data models are composed of entities, and entities are the objects and concepts whose data we want to track. They, in turn, become tables found in a database. Customers, products, manufacturers, and sellers are potential entities.

### 2. What Are the Three Types of Data Models?
The three types of data models:

    Physical data model - This is where the framework or schema describes how data is physically stored in the database.
    Conceptual data model - This model focuses on the high-level, user’s view of the data in question
    Logical data models - They straddle between physical and theoretical data models, allowing the logical representation of data to exist apart from the physical storage.

### 3. What is a Table?

A table consists of data stored in rows and columns. Columns, also known as fields, show data in vertical alignment. Rows also called a record or tuple, represent data’s horizontal alignment.

### 4. What is Normalization?

Database normalization is the process of designing the database in such a way that it reduces data redundancy without sacrificing integrity.

### 5. What Does a Data Modeler Use Normalization For?

The purposes of normalization are:

    Remove useless or redundant data
    Reduce data complexity
    Ensure relationships between the tables in addition to the data residing in the tables
    Ensure data dependencies and that the data is stored logically.


### 6. So, What is Denormalization, and What is its Purpose?

Denormalization is a technique where redundant data is added to an already normalized database. The procedure enhances read performance by sacrificing write performance.

### 7. What Does ERD Stand for, and What is it?

ERD stands for Entity Relationship Diagram and is a logical entity representation, defining the relationships between the entities. Entities reside in boxes, and arrows symbolize relationships

### 8. What’s the Definition of a Surrogate Key?

A surrogate key, also known as a primary key, enforces numerical attributes. This surrogate key replaces natural keys. Instead of having primary or composite primary keys, data modelers create the surrogate key, which is a valuable tool for identifying records, building SQL queries, and enhancing performance.

### 9. What Are the Critical Relationship Types Found in a Data Model? Describe Them.

The main relationship types are:

    Identifying. A relationship line normally connects parent and child tables. But if a child table’s reference column is part of the table’s primary key, the tables are connected by a thick line, signifying an identifying relationship.
    Non-identifying. If a child table’s reference column is NOT a part of the table’s primary key, the tables are connected by a dotted line, signifying a no-identifying relationship.
    Self-recursive. A recursive relationship is a standalone column in a table connected to the primary key in the same table.


### 10. What is an Enterprise Data Model?

This is a data model that consists of all the entries required by an enterprise.

### 11.  What Are the Most Common Errors You Can Potentially Face in Data Modeling?

These are the errors most likely encountered during data modeling.

    Building overly broad data models: If tables are run higher than 200, the data model becomes increasingly complex, increasing the likelihood of failure
    Unnecessary surrogate keys: Surrogate keys must only be used when the natural key cannot fulfill the role of a primary key
    The purpose is missing: Situations may arise where the user has no clue about the business’s mission or goal. It’s difficult, if not impossible, to create a specific business model if the data modeler doesn’t have a workable understanding of the company’s business model
    Inappropriate denormalization: Users shouldn’t use this tactic unless there is an excellent reason to do so. Denormalization improves read performance, but it creates redundant data, which is a challenge to maintain.


### 12. Explain the Two Different Design Schemas.

The two design schema is called Star schema and Snowflake schema. The Star schema has a fact table centered with multiple dimension tables surrounding it. A Snowflake schema is similar, except that the level of normalization is higher, which results in the schema looking like a snowflake.

### 13. What is a Slowly Changing Dimension?

These are dimensions used to manage both historical data and current data in data warehousing. There are four different types of slowly changing dimensions: SCD Type 0 through SCD Type 3.

### 14. What is Data Mart?

A data mart is the most straightforward set of data warehousing and is used to focus on one functional area of any given business. Data marts are a subset of data warehouses oriented to a specific line of business or functional area of an organization (e.g., marketing, finance, sales). Data enters data marts by an assortment of transactional systems, other data warehouses, or even external sources.

### 15. What is Granularity?

Granularity represents the level of information stored in a table. Granularity is defined as high or low. High granularity data contains transaction-level data. Low granularity has low-level information only, such as that found in fact tables.

### 16. What is Data Sparsity, and How Does it Impact Aggregation?

Data sparsity defines how much data we have for a model’s specified dimension or entity. If there is insufficient information stored in the dimensions, then more space is needed to store these aggregations, resulting in an oversized, cumbersome database.

### 17. What Are Subtype and Supertype Entities?

Entities can be broken down into several sub-entities or grouped by specific features. Each sub-entity has relevant attributes and is called a subtype entity. Attributes common to every entity are placed in a higher or super level entity, which is why they are called supertype entities.

### 18.  In the Context of Data Modeling, What is the Importance of Metadata?

Metadata is defined as “data about data.” In the context of data modeling, it’s the data that covers what types of data are in the system, what it’s used for, and who uses it.



Technical Metadata- This type specifies the database system and tables' names, table sizes, values, attributes, data types, etc. It also contains constraint details such as primary, foreign, and indexes.

Business Metadata- This data is business-specific and identifies data rights, business norms and standards, policies, and so on.

Descriptive Metadata- Descriptive Metadata delivers information on a folder, file, image, book, or movie. Title, date, size, author, etc., are all examples of information.

Operational Metadata- This type of metadata contains information on any corporate operation and is needed by managers and executives to accomplish any activity.

### 19. Should All Databases Be Rendered in 3NF?

No, it’s not an absolute requirement. However, denormalized databases are easily accessible, easier to maintain, and less redundant.

### 20. What’s the Difference Between forwarding and Reverse Engineering, in the Context of Data Models?

Forward engineering is a process where Data Definition Language (DDL) scripts are generated from the data model itself. DDL scripts can be used to create databases. Reverse Engineering creates data models from a database or scripts. Some data modeling tools have options that connect with the database, allowing the user to engineer a database into a data model.

### 21. What Are Recursive Relationships, and How Do You Rectify Them?

Recursive relationships happen when a relationship exists between an entity and itself. For instance, a doctor could be in a health center’s database as a care provider, but if the doctor is sick and goes in as a patient, this results in a recursive relationship. You would need to add a foreign key to the health center’s number in each patient’s record.

### 22.  What’s a Confirmed Dimension?

If a dimension is confirmed, it’s attached to at least two fact tables.

### 23. Why Are NoSQL Databases More Useful than Relational Databases?

NoSQL databases have the following advantages:

    They can store structured, semi-structured, or unstructured data
    They have a dynamic schema, which means they can evolve and change as quickly as needed
    NoSQL databases have sharding, the process of splitting up and distributing data to smaller databases for faster access
    They offer failover and better recovery options thanks to the replication
    It’s easily scalable, growing or shrinking as necessary


### 24. What’s a Junk Dimension?

This is a grouping of low-cardinality attributes like indicators and flags, removed from other tables, and subsequently “junked” into an abstract dimension table. They are often used to initiate Rapidly Changing Dimensions within data warehouses.

### 25. If a Unique Constraint Gets Applied to a Column, Will It Generate an Error If You Attempt to Place Two Nulls in It?

No, it won’t, because null error values are never equal. You can put in numerous null values in a column and not generate an error.

### 26. Explain the fact and fact table

The fact represents quantitative data. For example, the net amount which is due. A fact table contains numerical data as well as foreign keys from dimensional tables.

### 27.  Explain dimension and attribute

Dimensions represent qualitative data. For example, product, class, plan, etc. A dimension table has textual or descriptive attributes. For example, the product category and product name are two attributes of the product dimension table.

### 28. What is the fact less fact?

Fact less fact is a table having no fact measurement. It contains only the dimension keys.

### 29. What is in-memory analytics?

In-memory analytics is a process of caching the database in RAM.

### 30. What is the difference between OLTP and OLAP?

OLTP: procesamiento de transacciones en línea es un tipo de procesamiento de datos que consiste en ejecutar una serie de transacciones que ocurren simultáneamente 
OLAP: procesamiento analítico en línea cuyo objetivo es agilizar la consulta de grandes cantidades de datos. Para ello utiliza estructuras de datos diversas, normalmente multidimensionales

Por lo tanto, OLTP es un sistema de modificación de datos en línea, mientras que OLAP es un sistema de almacén de datos multidimensional histórico en línea que se utiliza para recuperar datos de grandes cantidades con fines analíticos.

|OLTP |OLAP |
|---|----|
| It is characterized by a large number of short online transactions.|It is characterized by a large volume of data. |
| OLTP is an online transactional system.| OLAP is an online analysis and data retrieving process. |
| OLTP uses traditional DBMS.| OLAP uses a data warehouse. |
| Tables in OLTP database are normalized.|The tables in OLAP are not normalized. |
| Its response time is in a millisecond.|Its response time is in second to minutes. |
|OLTP is designed for real time business operations. |OLAP is designed for the analysis of business measures by category and attributes. |

### 31. Define data sparsity

Data sparsity is a term used for how much data you have for entity/ dimension of the model

### 32. What is composite primary key?

Composite primary key is referred to the case where more than one table column is used as a part of primary key.

### 33. What is primary key?

Primary key is a column or group of columns that unequally identify each and every row in the table. The value of primary key must not be null. Every table must contain one primary key.

### 34. Explain foreign key

Foreign key is a group of attributes which is used to link parent and child table. The value of the foreign key column, which is available in the child table, is referred to the value of the primary key in the parent table.

### 35. What are the examples of the OLTP system?

Example of OLTP system are:

    Sending a text message
    Add a book to shopping cart
    Online airline ticket booking
    Online banking
    Order entry


### 36. List out the types of normalization?

Types of normalizations are: 1) first normal form, 2) second normal form, 3) third normal forms, 4) boyce-codd fourth, and 5) fifth normal forms.

### 37. What is forward data engineering?

Forward engineering is a technical term used to describe the process of translating a logical model into a physical implement automatically.


### 38. What is PDAP?

It is a data cube that stores data as a summary. It helps the user to analyse data quickly. The data in PDAP is stored in a way that reporting can be done with ease.

### 39. Explain snow flake schema database design

A snowflake schema is an arrangement of a dimension table and fact table. Generally, both tables are further broken down into more dimension tables.

### 40. Explain analysis service

Analysis service gives a combined view of the data that is used in data mining or OLAP.

### 41. What is sequence clustering algorithm?

Sequence clustering algorithm collects paths which are similar or related to each other and sequences of data having events.

### 42.  What is discrete and continuous data?

Discreet data is a finite data or defined data. E.g., gender, telephone numbers. Continuous data is data that changes in a continuous and ordered manner. E.g., age.

### 43. What is the time series algorithm?

Time series algorithm is a method to predict continuous values of data in table. E.g., Performance one employee can forecast the profit or influence.

### 44. What is Business Intelligence?

BI (Business Intelligence) is a set of processes, architectures, and technologies that convert raw data into meaningful information that drives profitable business actions. It is a suite of software and services to transform data into actionable intelligence and knowledge.

### 45. What is bit mapped index?

Bitmap indexes are a special type of database index that uses bitmaps (bit arrays) to answer queries by executing bitwise operations.

### 46. Explain data warehousing in detail

Data warehousing is a process for collecting and managing data from varied sources. It provides meaningful business enterprise insights. Data warehousing is typically used to connect and analyse data from heterogeneous sources. It is the core of the BI system, which is built for data analysis and reporting.

### 47. What is junk dimension?

Junk dimension combines two or more related cardinality into one dimension. It is usually Boolean or flag values.

### 48. Explain data collection frequency

Data collection frequency is the rate to collect the data. It also passes through various stages. These stages are: 1) extracting from various sources, 3) transforming, 4) cleansing, and 5) storing.

### 49. What is database cardinality?

Cardinality is a numerical attribute of the relationship between two entities or entity sets.

### 50.  What are the different types of cardinal relationships?

Different types of key cardinal relationships are:

    One-to-One Relationships
    One-to-Many Relationships
    Many-to-One Relationships
    Many-to-Many Relationships


### 51. Define Critical Success Factor and list its four types

Critical Success Factor is a favorable result of any activity needed for organization to reach its goal.

Four types of critical success factor are:

    Industry CSFs
    Strategy CSFs
    Environmental CSFs
    Temporal CSFs


### 52.  What is data mining?

Data mining is a multi-disciplinary skill that uses machine learning, statistics, AI, and database technology. It is all about discovering unsuspected / previously unknown relationships amongst the data.

### 53.  What is identifying relationship?

Identifying entity relationships in DBMS is used to identify a relationship between two entities: 1) strong entity, and 2) weak entity.

### 54. What is predictive modelling analytics?

The process of validating or testing a model which would used to predict testing and validating outcomes. It can be used for machine learning, artificial intelligence, as well as statistics.

### 55. What are the different types of constraints?

A different type of constraint could be unique, null values, foreign keys, composite key or check constraint, etc.

### 56. What is a data-modelling tool?

Data modelling tool is a software that helps in constructing data flow and the relation between data. Examples of such tools are Borland Together, Altova Database Spy, casewise, Case Studio 2, etc.

### 57. What is hierarchical DBMS?

In the hierarchical database, model data is organized in a tree-like structure. Data is stored in a hierarchical format. Data is represented using a parent-child relationship. In hierarchical DBMS parent may have many children, children have only one parent.

### 58. What are the drawbacks of the hierarchical data model?

The drawbacks of the hierarchical data model are:

    It is not flexible as it takes time to adapt to the changing needs of the business.
    The structure poses the issue in, inter-departmental communication, vertical communication, as well as inter-agency communication.
    Hierarchical data model can create problems of disunity.


### 59. Explain the process-driven approach of data modelling

Process-driven approach used in data modelling follows a step by step method on the relationship between the entity-relationship model and organizational process.

### 60. What are the characteristics of a logical data model?

Characteristics of logical data model are:

    Describes data needs for a single project but could integrate with other logical data models based on the scope of the project.
    Designed and developed independently from the DBMS.
    Data attributes will have datatypes with exact precisions and length.
    Normalization processes to the model, which is generally are applied typically till 3NF.


### 61. What are the characteristics of physical data model?

Characteristics of physical data model are:

    The physical data model describes data need for a single project or application. It may be integrated with other physical data models based on project scope.
    Data model contains relationships between tables that address cardinality and nullability of the relationships.
    Developed for a specific version of a DBMS, location, data storage, or technology to be used in the project.
    Columns should have exact datatypes, lengths assigned, and default values.
    Primary and foreign keys, views, indexes, access profiles, and authorizations, etc. are defined.


### 62. What are the two types of data modelling techniques?

Two types of data modelling techniques are: 1) entity-relationship (E-R) Model, and 2) UML (Unified Modelling Language).

### 63. What is UML?

UML (Unified Modelling Language) is a general-purpose, database development, modelling language in the field of software engineering. The main intention is to provide a generalized way to visualize system design.

### 64. Explain object-oriented database model

The object-oriented database model is a collection of objects. These objects can have associated features as well as methods.

### 65. What is a network model?

It is a model which is built on hierarchical model. It allows more than one relationship to link records, which indicates that it has multiple records. It is possible to construct a set of parent records and child records. Each record can belong to multiple sets that enable you to perform complex table relationships.

### 66. What is hashing?

Hashing is a technique which is used to search all the index value and retrieve desired data. It helps to calculate the direct location of data, which are recorded on disk without using the structure of the index.

### 67. What is business or natural keys?

business or natural keys is a field that uniquely identifies an entity. For example, client ID, employee number, email etc.

### 68. What is compound key?

When more than one field is used to represent a key, it is referred to as a compound key.

### 69. Explain alternate key in detail

Alternate key is a column or group of columns in a table that uniquely identifies every row in that table. A table can have multiple choices for a primary key, but only one can be set as the primary key. All the keys which are not primary key are called an Alternate Key.

### 70. List out popular DBMS software

Popular DBMS software is:

    MySQL
    Microsoft Access
    Oracle
    PostgreSQL
    dbase
    FoxPro
    SQLite
    IBM DB2
    Microsoft SQL Server.


### 71. Explain various types of fact tables

There are three types of fact tables:

    Additive: It is a measure that is added to any dimension.
    Non-additive: It is a measure that can’t be added to any dimension.
    Semi-additive: It is a measure that can be added to a few dimensions.

### 72. What is aggregate table?

The aggregate table contains aggregated data that can be calculated using functions such as: 1) Average 2) MAX, 3) Count, 4) SUM, 5) SUM, and 6) MIN.

### 73. List types of Hierarchies in data modelling

There are two types of Hierarchies: 1) Level based hierarchies and 2) Parent-child hierarchies.

### 74. Data Warehouse vs Data Mart – Difference Between Them
Data Warehouse is a large repository of data collected from different sources, whereas Data Mart is only subtype of a data warehouse.
Data Warehouse is focused on all departments in an organization, whereas Data Mart focuses on a specific group.
Data Warehouse designing process is complicated, whereas the Data Mart process is easy to design.
### 75. What is XMLA?

XMLA is an XML analysis that is considered as standard for accessing data in Online Analytical Processing (OLAP).

### 76. Explain chained data replication

The situation when a secondary node selects target using ping time or when the closest node is a secondary, it is called as chained data replication.

### 77. Explain Virtual Data Warehousing

A virtual data warehouse gives a collective view of the completed data. A virtual data warehouse does not have historical data. It is considered as a logical data model having metadata.

### 78. Explain snapshot of data warehouse

Snapshot is a complete visualization of data at the time when data extraction process begins.

### 79.  What is a bi-directional extract?

The ability of system to extract, cleanse, and transfer data in two directions is called as a directional extract.

### 80. What does "data sparsity" imply?

The number of blank cells in a database is known as data sparsity. In a data model, it describes the amount of data that is available for a specific dimension. Due to a lack of information, saving aggregations consumes a lot of space.

### 81. Explain the concepts of subtypes and supertypes.

Entities can be split into sub-entities and classified according to their characteristics. Each sub-entity, also known as a subtype entity, has its own set of properties.

Some qualities are unique to each entity and are only found in higher or super-level entities. This is why they are referred to as supertype entities.

### 82. What is a fact table?
A fact table is the central table in a star schema of a data warehouse. A fact table stores quantitative information for analysis and is often denormalized.

A fact table works with dimension tables. A fact table holds the data to be analyzed, and a dimension table stores data about the ways in which the data in the fact table can be analyzed. 
### 83. Briefly define factless fact tables in data modeling.

A factless fact table is one that does not include any facts. They only have dimensional keys, and they capture events that occur only at the information level, not at the computation level (just information about an event that happens over a period). The many-to-many links between dimensions are captured in a factless fact table, containing no numeric or textual facts. They're commonly used to document events or information about coverage.

Factless fact tables are useful for tracking a process or collecting data. There are two types of factless fact tables: one that describes occurrences and one that describes conditions.

### 84. Give a brief overview of the Critical Success Factor and its four types.

A critical success factor (CSF) is a certain aspect or element that a team, department, or company must effectively implement and emphasize to meet its strategic objectives. CSFs lead to an increased value for products and services and beneficial outcomes. The significance of crucial success factors stems from the fact that they serve as a roadmap for a company. The only way to know what the outputs entail is to analyze and define a critical success factor; otherwise, they stay fictional.

### 85. What do you mean by the CAP Theorem? How does it work?

The CAP theorem shows that no distributed system can ensure C, A, and P at the same time. To put it another way, it states that a distributed system cannot deliver over two of the three assurances.

Consistency: After an activity, the data should stay consistent. After upgrading the database, for example, all of our queries should return the same result.

Availability: There should be no downtime with the database; it should always be accessible and active.

Partition Tolerance: Even if communication between the servers is not consistent, the system should remain functional.

### 86. What are the different critical relationship types in a data model?

A relationship mainly connects parent and child tables with each other. In a data model, there are three different types of critical relationships:

Identifying: In this type, the primary keys of the parent tables include a reference column of child tables, which is connected by a thick line and helps identify the entries. A thick line is frequently used to replace this relationship. Because the foreign key forms part of the primary key, they are referred to as identifying keys. There can't be a child object if there isn't a parent object.

Non-identifying: A child table's reference field does not exist in the parent table's primary key. A dotted line represents this relationship. Depending on the situation, this relationship can be optional or mandatory. It signifies that NULL can be allowed (if optional) or not allowed (if obligatory) in foreign key columns.

Self-recursive: In this case, a single column is linked to a table's primary key. This is a relationship that exists between different column objects belonging to a similar entity.

### 87. Explain the different types of dimensions with examples.

There are usually five different categories of dimensions-

a) Conformed dimensions: A conformed dimension is one that is used in multiple domains. You can use it with multiple fact tables in a particular database or even across multiple data marts/warehouses.

b) Role-Playing Dimensions: These are the dimensions in a database that serve various purposes.

c) Slowly Changing Dimension (SCD): SCDs are the most essential dimensions. These are the dimensions where the value of an attribute changes over time. SCDs are classified into five categories: type 0, type 1, type 2, type 3, and type 4.

d) Junk Dimension: This is a dimension table that contains attributes that don't belong in the fact table or any of the existing dimension tables. These dimensions have typical attributes such as flags or indications.

e) Degenerated Dimension: A degenerated dimension is not a fact yet appears as a primary key in the fact table. It doesn't have its own set of dimensions. A single attribute dimension table is another name for it.

### 88. Describe the features of a database management system.

    A multi-user environment is enabled by DBMS, allowing users to explore and process the data simultaneously.

    It adheres to the ACID principle (Atomicity, Consistency, Isolation, and Durability).

    It ensures security and eliminates redundancy.

    It enables multiple data views.

    Tables are built by DBMS by combining entities and their relationships.

    Data sharing and multiuser transaction processing are made easier using DBMS.


### 89. Mention some of the fundamental data models.

    Fully-Attributed (FA): This is a third normal form model that provides all of the data for a specific implementation approach.

    Transformation Model (TM): Specifies the transformation of a relational data model into a structure that is suitable for the DBMS in use. The TM is no more in the third normal form in the vast majority of cases. The structures are optimized depending on the DBMS's capabilities, data levels, and projected data access patterns.

    DBMS Model: The DBMS Model contains the database design for the system. For the complete integrated system, the DBMS Model can be at the project or area level.


### 90. Briefly define Normalization and the three normal forms- 1NF, 2NF, and 3NF.

In relational database design, normalization is the process of organizing data in a relational structure to reduce redundancy and non-relational structures. By deleting any model structures that allow various methods to know the same information, you can control and eliminate data redundancy by following the normalization criteria.

    First Normal Form (1NF)- The entity E is in first normal form (INF) if and only if all underlying values include only atomic values. You must remove any recurring sets (such as those found in legacy COBOL data structures).

    Second Normal Form (2NF)- If an entity E is in 1NF and every non-key attribute depends entirely on the primary key, it is in 2NF. In other words, there are no partial key dependencies; rather, dependence is on the full key K of E, not on a specific subset of K.

    Third Normal Form (3NF)- If an entity E is in 2NF and no non-key attribute of E depends on another non-key attribute, it is in 3NF. Another way to think about it is that if an entity E is in 2NF and every non-key attribute is non-transitive relying on the main key, it is in 3NF.


### 91. What are the various types of measures available for fact tables?

There are mainly three different types of measures available-

    Additive measures- The most popular type of measure is additive, which can be aggregated throughout all of the dimensions in the fact table. Additive measures are used to sum data across multiple dimensions.

    Semi-additive measures- Semi-additive measures are the ones you can aggregate across some dimensions, but not all. Semi-additive measures, for example, include head counts and inventories.

    Non-additive measures- You cannot aggregate non-additive measures over any of the dimensions. You can't logically combine these measures across records or fact rows. Non-additive measures are mostly calculated using ratios or other mathematical methods. For such a measure, the only analysis possible is to count the number of rows.


### 92. What is Amazon's RDBMS service?

The Amazon Relational Database Service is a web service for setting up, managing and scaling a relational database in the cloud. Standard relational database engines are supported by Amazon RDS, which is controlled, extended, and available on-demand. RDS handles time-consuming management operations, allowing you to focus on your application rather than your database

### 93. What is Amazon Aurora?

Amazon Aurora is a high-availability, automated failover relational database engine that supports MySQL and PostgreSQL. To put it another way, Amazon Aurora is a hybrid of MySQL and Postgres. Aurora is a multi-threaded, multiprocessor database engine that prioritizes performance, availability, and operational efficiency.

Amazon Aurora differs from typical MySQL and Postgres database engines in that it does not employ a Write-Ahead Log, but it does feature a crash recovery scheme. Amazon also provides the feature to duplicate data from an Amazon Aurora database to a MySQL or Postgres database on the same instance, as well as vice versa, allowing you to employ the two databases together.

### 94. What is the function of Amazon Redshift?

    Amazon Redshift is a cloud-based data warehousing solution that is quick, fully managed, and extends to petabytes.

    It enables you to examine all of your data quickly and effectively using your existing business intelligence tools.

    Amazon Redshift allows you to access data using conventional SQL and integrates with a variety of business intelligence applications, including Tableau, MicroStrategy, QlikView, and others.


### 95. What is the difference between Amazon DynamoDB and other NoSQL databases?

Amazon DynamoDB is a cloud-based database with no physical location. It is scalable enough to suit the needs of high-performance applications. You can set up security, back up all in case of a crash or issues, save data in various locations, and even export all of your data if you want to.

Amazon DynamoDB is a hosted database for applications that require regular updates without the assistance of a database administrator. DynamoDB takes care of all database administration on their servers, minimizing the need for manual tasks like backups and replication.

### 96. Explain the differences between the DataStage Server's Hashed file stage and the Sequential file stage.

    We use a hashed file on the Datastage server to store information on the hash algorithms and the hash key value. On the other hand, a sequential file lacks a key value for data storage.

    Reading or writing data from one or more flat files becomes easier using a sequential file stage. The hashed file stage is helpful for data extraction within a DataStage job. Many inputs or outputs may be present at each stage of the hashed file process.


### 97. Define the term Data Skew.

When working with a large business with more than 10,000 records, you will come across the issue of data skew. Experts refer to a situation as "ownership data skew" when a single person owns many records. Due to "data skew," these users will have performance issues when performing updates. This occurs when the majority of the records for a specific object are owned by a single user or members of a single role.

### 98. What happens to the detail record after deleting the master record? What happens to the child record when the parent record is removed?

When a master record is deleted in a master-detail relationship, the detail record is also immediately deleted (Cascade delete).

The child record in a Lookup relationship won't be removed, even if the parent record is.

### 99. Is it possible to have a roll-up summary field in a master-detail relationship?

Yes. A roll-up summary is an option if there is a master-detail relationship. However, a lookup relationship is an exception.


### 100. Define Virtual Data Warehouses.

A virtual data warehouse provides a unified overview of the final data. Historical data is missing from a virtual data warehouse. It is defined as a logical data model with metadata.

### 101. Explain column store databases and in-memory analytics.

A database can now store and retrieve data using a column store. A database's column store is a contemporary method for storing and retrieving data. These days, column store (or columnar store) databases use column-oriented storage, which stores the data vertically. Since the database reads the columns, a query contains, fewer hard disk reads are necessary to retrieve data.

### 102. What is real-time data warehousing?

Real-time data warehousing refers to a system that continuously reflects the status of the warehouse. Suppose you execute a query on the real-time data warehouse to find out more about a specific feature of the warehouse or entity it describes. In that case, the result will reflect that entity's status when the query was run. Most warehouses contain highly latent data representing the business during a specific period. Low latency current (or real-time) data is provided through a real-time data warehouse.

### 103. 

### 104. 

### 105. 

### 106. 

### 107. 

### 108. 

### 109. 

### 110. 

### 111. 

### 112. 

### 113. 

### 114. 

### 115. 

### 116. 

### 117. 

### 118. 

### 119. 

### 120. 

### 121. 

### 122. 

### 123. 

### 124. 

### 125. 

### 126. 

### 127. 

### 128. 

### 129. 

### 130. 

### 131. 

### 132. 

### 133. 

### 134. 

### 135. 

### 136. 

### 137. 

### 138. 

### 139. 

### 140. 

### 141. 

### 142. 

### 143. 

### 144. 

### 145. 

### 146. 

### 147. 

### 148. 

### 149. 
