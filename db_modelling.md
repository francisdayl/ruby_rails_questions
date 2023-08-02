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

### 103. Give us a non-computer example of preemptive and non-preemptive scheduling

Consider any system where people use some kind of resources and compete for them. The non-computer examples for preemptive scheduling the traffic on the single-lane road if there is an emergency or there is an ambulance on the road the other vehicles give a path to the vehicles that are in need.

### 104.  Why are recursive relationships are bad? How do you resolve them?

Recursive relationships are an interesting and more complex concept than the relationships you have seen in the previous chapters, such as one-to-one, one-to-many, and many-to-many. A recursive relationship occurs when there is a relationship between an entity and itself.

For example, a one-to-many recursive relationship occurs when an employee is the manager of another employee. The employee entity is related to itself, and there is a one-to-many relationship between one employee (the manager) and many other employees (the people who report to the manager).

Because of the more complex nature of these relationships, we will need slightly more complex methods of mapping them to a schema and displaying them in a style sheet.

### 105.  Is this statement TRUE or FALSE? all databases must be in third normal form?

In general, all organization databases are normalized to 3nf in order to remove redundancy and efficient access. A database can also be created without normalization. Hence it is not mandatory that a database should be in 3nf.

### 106. What are some of the common mistakes encountered in data modelling?

Some of the mistakes encountered in data modelling are:

Building massive data models: As good practices, a data model is recommended to have <=200 tables. This is because large data models are more likely to have design faults.
Lack of purpose: When the purpose of the business solution is not clear, then the data model generated would be incorrect as there is no means of validating the correctness of the model against the organization objectives.
Unnecessary de-normalization: Denormalization should not be done unless we have a solid business reason as it contributes to data redundancy which might increase the cost of maintenance.
Unnecessary surrogate keys: Surrogate keys are generated artificially for identifying the records. Too much use of these keys is not recommended when the natural keys can serve the purpose.

### 107. What is a distributed database?

A distributed database is a database that is spread out across multiple locations, often on different servers. This can be done for a variety of reasons, such as to improve performance or to increase availability.

### 108. Can you explain what data distribution is in the context of databases?

In a distributed database, data is physically stored across multiple computers that are connected together in a network. This allows for greater scalability and availability than a traditional, single-computer database.

### 109. How do you define a distributed system?

A distributed system is a system where components are spread out across a network and interact with each other to achieve a common goal.

### 110. What are some features oif a distributed database?

A distributed database is a database that is spread out across multiple locations. This can be done for a variety of reasons, such as to improve performance or to increase availability. Some features of a distributed database include the ability to replicate data across multiple locations, the ability to partition data across multiple locations, and the ability to manage data across multiple locations.

### 111. What are the main advantages and disadvantages of using a distributed database?

The main advantage of using a distributed database is that it can provide better performance and availability than a traditional centralized database. The main disadvantage is that it can be more complex to manage and maintain.

### 112.  Are there different types of distributed databases? If yes, then which ones have you worked with?

Yes, there are different types of distributed databases. I have worked with two main types: shared-nothing and shared-disk. In a shared-nothing distributed database, each node has its own private storage and there is no central storage that is shared by all nodes. This type of database is typically more scalable and can handle more concurrent users than a shared-disk database. In a shared-disk database, all nodes have access to a common storage area, such as a SAN or NAS. This type of database is typically easier to manage than a shared-nothing database, but is not as scalable.

### 113. What are the basic requirements for creating a distributed database?

In order to create a distributed database, you will need to have a database management system that supports distributed databases, as well as multiple computers that are connected to each other. The computers will need to be able to share data and access the same database management system.

### 114. What is the difference between centralized databases and distributed databases?

A centralized database is one in which all data is stored in a single location. A distributed database is one in which data is stored across multiple locations, often on different servers. The main advantage of a distributed database is that it can be more scalable than a centralized database, as it can more easily accommodate growth.

### 115.  Is it possible to replicate data from one node to another? If yes, how would you go about doing that?

Yes, it is possible to replicate data from one node to another. There are a few different ways to do this, but one common method is to use a tool like rsync. Rsync is a tool that can be used to synchronize files and directories between two different locations. In this case, you would use it to replicate the data from one node to another.

### 116. What’s your understanding of consistency in the context of distributed databases?

Consistency in a distributed database means that all nodes in the system contain the same data. This is usually achieved through replication, where each node contains a copy of the data.

### 117. What is the best way to ensure fault tolerance in a distributed database?

There are a few different ways to ensure fault tolerance in a distributed database, but the most common method is to use replication. This involves having multiple copies of the same data stored in different locations. If one copy of the data is lost or corrupted, then the other copies can be used to restore the data.

### 118. Does sharding make sense when designing a distributed database?

Sharding can be a helpful way to improve performance in a distributed database by distributing data across multiple servers. However, it is important to consider whether sharding makes sense for your particular application before implementing it, as it can complicate your database design and add overhead.

### 119. What is Sharding?

Sharding is a database architecture pattern related to horizontal partitioning — the practice of separating one table’s rows into multiple different tables, known as partitions. Each partition has the same schema and columns, but also entirely different rows. Likewise, the data held in each is unique and independent of the data held in other partitions.

Sharding involves breaking up one’s data into two or more smaller chunks, called logical shards. The logical shards are then distributed across separate database nodes, referred to as physical shards, which can hold multiple logical shards. Despite this, the data held within all the shards collectively represent an entire logical dataset.

It can be helpful to think of horizontal partitioning in terms of how it relates to vertical partitioning. In a vertically-partitioned table, entire columns are separated out and put into new, distinct tables. The data held within one vertical partition is independent from the data in all the others, and each holds both distinct rows and columns. The following diagram illustrates how a table could be partitioned both horizontally and vertically:

The main appeal of sharding a database is that it can help to facilitate horizontal scaling, also known as scaling out. Horizontal scaling is the practice of adding more machines to an existing stack in order to spread out the load and allow for more traffic and faster processing. This is often contrasted with vertical scaling, otherwise known as scaling up, which involves upgrading the hardware of an existing server, usually by adding more RAM or CPU.

### 120. How many sharding architechtures there are?
- Key Based Sharding: also known as hash based sharding, involves using a value taken from newly written data — such as a customer’s ID number, a client application’s IP address, a ZIP code, etc. and plugging it into a hash function to determine which shard the data should go to. A hash function is a function that takes as input a piece of data (for example, a customer email) and outputs a discrete value, known as a hash value. In the case of sharding, the hash value is a shard ID used to determine which shard the incoming data will be stored on. 
To ensure that entries are placed in the correct shards and in a consistent manner, the values entered into the hash function should all come from the same column. This column is known as a shard key. In simple terms, shard keys are similar to primary keys in that both are columns which are used to establish a unique identifier for individual rows. Broadly speaking, a shard key should be static, meaning it shouldn’t contain values that might change over time. Otherwise, it would increase the amount of work that goes into update operations, and could slow down performance.

- Range based sharding:  involves sharding data based on ranges of a given value. To illustrate, let’s say you have a database that stores information about all the products within a retailer’s catalog. You could create a few different shards and divvy up each products’ information based on which price range they fall into, like this
The main benefit of range based sharding is that it’s relatively simple to implement. Every shard holds a different set of data but they all have an identical schema as one another, as well as the original database. The application code reads which range the data falls into and writes it to the corresponding shard.

- Directory Based Sharding: To implement directory based sharding, one must create and maintain a lookup table that uses a shard key to keep track of which shard holds which data. A lookup table is a table that holds a static set of information about where specific data can be found
The main appeal of directory based sharding is its flexibility. Range based sharding architectures limit you to specifying ranges of values, while key based ones limit you to using a fixed hash function which, as mentioned previously, can be exceedingly difficult to change later on. Directory based sharding, on the other hand, allows you to use whatever system or algorithm you want to assign data entries to shards, and it’s relatively easy to dynamically add shards using this approach.

While directory based sharding is the most flexible of the sharding methods discussed here, the need to connect to the lookup table before every query or write can have a detrimental impact on an application’s performance. Furthermore, the lookup table can become a single point of failure: if it becomes corrupted or otherwise fails, it can impact one’s ability to write new data or access their existing data.


### 121. When you should shard? 
sharding is usually only performed when dealing with very large amounts of data. Here are some common scenarios where it may be beneficial to shard a database:

The amount of application data grows to exceed the storage capacity of a single database node.
The volume of writes or reads to the database surpasses what a single node or its read replicas can handle, resulting in slowed response times or timeouts.
The network bandwidth required by the application outpaces the bandwidth available to a single database node and any read replicas, resulting in slowed response times or timeouts
### 122. How can you avoid sharding?
Before sharding, you should exhaust all other options for optimizing your database. Some optimizations you might want to consider include:

Setting up a remote database. If you’re working with a monolithic application in which all of its components reside on the same server, you can improve your database’s performance by moving it over to its own machine. This doesn’t add as much complexity as sharding since the database’s tables remain intact. However, it still allows you to vertically scale your database apart from the rest of your infrastructure.
Implementing caching. If your application’s read performance is what’s causing you trouble, caching is one strategy that can help to improve it. Caching involves temporarily storing data that has already been requested in memory, allowing you to access it much more quickly later on.
Creating one or more read replicas. Another strategy that can help to improve read performance, this involves copying the data from one database server (the primary server) over to one or more secondary servers. Following this, every new write goes to the primary before being copied over to the secondaries, while reads are made exclusively to the secondary servers. Distributing reads and writes like this keeps any one machine from taking on too much of the load, helping to prevent slowdowns and crashes. Note that creating read replicas involves more computing resources and thus costs more money, which could be a significant constraint for some.
Upgrading to a larger server. In most cases, scaling up one’s database server to a machine with more resources requires less effort than sharding. As with creating read replicas, an upgraded server with more resources will likely cost more money. Accordingly, you should only go through with resizing if it truly ends up being your best option.

### 123. What is a Shared-nothing architecture?
is a distributed computing architecture in which each update request is satisfied by a single node (processor/memory/storage unit) in a computer cluster. The intent is to eliminate contention among nodes. Nodes do not share (independently access) the same memory or storage. One alternative architecture is shared everything, in which requests are satisfied by arbitrary combinations of nodes. This may introduce contention, as multiple nodes may seek to update the same data at the same time.

### 124. What is horizontal scaling? Why is it important in the context of distributed databases?

Horizontal scaling is the process of adding more nodes to a system in order to increase its capacity or performance. In the context of distributed databases, horizontal scaling is important because it allows the database to continue to function even if one or more of its nodes fail. By adding more nodes, the database can continue to operate as long as there are still nodes remaining.

### 125. What do you understand about indexing on a distributed database?

Indexing on a distributed database is a process of creating and storing a data structure that can be used to quickly locate specific records within the database. This data structure is typically a tree or a hash table, and it can be used to speed up the process of searching for records by allowing the database to quickly narrow down the search space.

### 126. What is a load balancer? What is its role in a distributed database?

A load balancer is a device that helps to distribute traffic evenly across a network of servers. In a distributed database, the load balancer helps to ensure that each server in the network is able to handle its share of traffic and requests. This helps to prevent any one server from becoming overloaded and ensures that the database as a whole is able to function properly.

### 127. How can you implement ACID compliance in a distributed database?

In order to implement ACID compliance in a distributed database, you need to use a two-phase commit protocol. This ensures that all of the nodes in the distributed database are in sync and that any changes that are made to the database are made in a consistent manner

### 128. What are some common use cases for distributed databases?

There are many potential use cases for distributed databases. Some common examples include organizations with multiple locations that need to share data, companies that need to share data with partners or suppliers, or any situation where data needs to be shared across a wide area network.

### 129. What are the major differences between a cloud-based database and an on-premise distributed database?

The biggest difference between a cloud-based database and an on-premise distributed database is that the former is hosted on a remote server, while the latter is hosted on a local server. This means that a cloud-based database is more scalable and can be accessed from anywhere, while an on-premise distributed database may be more expensive to set up and maintain.

### 130. What is a NoSQL database? Do they fall under the umbrella of distributed databases?

NoSQL databases are a type of database that does not use the traditional relational model. Instead, they use a more flexible schema-less model. This makes them well-suited for handling large amounts of data that may be constantly changing. While NoSQL databases can be distributed, not all of them are.

### 131. What is scale out in the context of distributed databases?

Scale out is the process of adding more nodes to a distributed database in order to increase capacity or performance. This can be done by adding more servers, storage devices, or other components to the system.

### 132. what is partitioning (vertical partitioning)
In vertical partitioning, a table is split vertically. The table is divided for colums. lets suppose that there is a table named "College" with the fields: "id", "College_name, ranking, num_students, num_teachers"
We can make a partitionate that table into 2 tables, Table *A* can have the fields "id", "college_name" and "ranking" while table B can have "id", "num_students" and "num_teachers"
Both of the partitions have a shared key which is used to bridge the connection between related data, but the two vertical partitions do not have the same schema.


### 133. What is database replication?
Database replication is the frequent electronic copying of data from a database in one computer or server to a database in another -- so that all users share the same level of information. The result is a distributed database in which users can quickly access data relevant to their tasks without interfering with the work of others. Numerous elements contribute to the overall process of creating and managing database replication.

### 134. How database replication works
Database replication can either be a single occurrence or an ongoing process. It involves all data sources in an organization's distributed infrastructure. The organization's distributed management system is used to replicate and properly distribute the data amongst all the sources.

### 134. How To Perform Database Replication
For an easy understanding of how to perform database replication, the database replication process can be broken down into the steps listed below (a much simplified version):

    The first thing to do is to identify your data source and where you want to replicate it too. 
    Determine the files, folders, and applications that will be copied, if applicable.
    Select a suitable type of replication from the ones listed above that will meet your business needs.
    State and acknowledge how often you want an update on the replication be it scheduled or in real-time and either in batches or in bulk.
    You can now proceed to set up the data replication by writing a custom application or by using one of many available replication tools that can give you your desired outcome.
    Finally, monitor the replication process to ensure that the data is replicated consistently and as expected to ensure data quality.     

### 135. Database replication techniques
- Asynchronous: replication is when the data is sent to the model server -- the server that the replicas take data from -- from the client. Then, the model server pings the client with confirmation saying the data has been received. From there, it goes about copying data to the replicas at an unspecified or monitored pace.
- Synchronous: replication is when data is copied from the client server to the model server and then replicated to all the replica servers before the client is notified that data has been replicated. This takes longer to verify than the asynchronous method, but it presents the advantage of knowing that all data was copied before proceeding.

### 135. types Database replication techniques
There are different types of database replication that can be applied. Choosing a particular type of replication will largely depend on your business and what you want to do with the data. Below is an explanation of each of the types of database replication.

- *Full-table replication:* Full-table replication copies everything from the source database to the destination storage. It transfers new, updated, and existing rows from the publisher to the subscriber. It enables hard-deletes operations but this method of replication is associated with a high cost of maintenance since the processing power and network bandwidth requirements needed to copy everything is high. It places a burden on the network and can cause delays in replication especially when the data volume is large. 
- *Snapshot replication: *This type of database replication takes a snapshot of the source database and replicates the data in the target destination database. It does not regard changes made on data such as new, updated, or deleted, rather, it makes a copy of what it captures at that given time. This mode of replication is preferably used when changes made to the data are infrequent. It is faster than full-table replication but does not keep records of the hard-deleted data.
- *Merge replication:* Merge replication merges two or more databases into a single database. It is commonly found in server-to-client models and allows independent changes to be made by both the publisher and subscriber.
- *Key-based incremental replication:* This method of replication scans keys or indexes in a DBMS to check for changes such as delete, new, and updated. The replication process then replicates only the relevant replication keys to the replica database to reflect the changes since the last update. These keys are typically a timestamp, datestamp, or integer. The process is fast since only marked changes are copied to the replica database. Unfortunately, this approach does not support hard-deletes as the key value is also deleted when the record is deleted in the primary database.
- *Log-based incremental replication:* This replication type copies data based on the database binary log file. The binary log file, when scanned, provides information on changes such as inserts, updates, and deletes that have occurred in the primary database. These same changes are then implemented in the destination database. This is the most popular solution since it is very efficient for static databases and is supported by most database vendors including MySQL, PostgreSQL, Oracle, and MongoDB.
- *Transactional replication:* Transactional replication first copies all the existing data from the source database into the destination location then with any new development in the source data, the same transaction is executed in the replicas. Though it is an efficient approach to replication, the replicas are mostly used for read operations, and may not support create, delete, and update operations.

### 136. types of database replication based on the type of server 
- Single-leader architecture is one server that receives writes from clients, and replicas draw data from there. This is the most common and classic method. It's a synchronized method, but somewhat inflexible.
- Multi-leader architecture is multiple servers that can receive writes and serve as a model for replicas. It is beneficial for when replicas are spread out and leaders must be near all of them to prevent latency.
- No-leader architecture is every server that can receive writes and serve as a model for replicas. This was pioneered by Amazon's DynamoDB. While it offers maximum flexibility, it poses challenges for synchronization.
### 137. Advantages and disadvantages of database replication
#### Advantages
- Load reduction. Because replicated data can be spread over several servers, it eliminates the likelihood that any one server will be overwhelmed with user queries for data.
- Efficiency. Servers that are less burdened with queries can offer improved performance to fewer users.
- High availability. Employing multiple servers with the same data ensures high availability, meaning that if one server goes down, the entire system can still provide acceptable performance.
#### Disadvantages 
Many disadvantages of database replication stem from poor general data governance practices. These disadvantages include the following:

- Data loss. Data loss can occur during replication when incorrect data or iterations or updates of a database are copied and, consequently, important data is deleted or unaccounted for. This can happen if the primary key used to verify the quality of data in the replica is malfunctioning or incorrect. It can also occur if database objects are incorrectly configured within the source database.
- Data inconsistency. Similarly, incorrect or out-of-date replicas can cause different sources to be out of sync with each other. This may lead to wasted data warehouse costs that are spent needlessly analyzing and storing irrelevant data.
- Multiple servers. Running multiple servers has an inherent maintenance and energy cost associated. It requires either the organization or a third party to address these costs. If a third party handles them, the organization runs the risk of vendor lock-in or service issues beyond the organization's control.

### 138. Database replication vs. mirroring
- Mirroring of data, simply put, is the creation of a backup database server that acts as a safety net for the primary database. This is used to prevent loss of data in case anything happens to the primary database. The mirrored database kicks in to act as a primary database server when the primary database server is down. Traffic is immediately redirected back to the primary server immediately after it is restored. The mirrored database server does this only when the primary database server is out of service since only one of the two can be active at a given time.
- Database replication, on the other hand, is the process of copying and storing data from one database to several target databases found in different locations around the globe. It is also a very useful approach that is used, for example, with file servers as it helps users to search and locate files and access the files stored in servers closest to them. Whether you are replicating a database or some other type of storage, replication thrives in a distributed system.

### 139. Name some Database replication software
- *Qlik Replicate*. A software package that focuses on being easy to learn and implement, Replicate uses automation and log-based capture to minimize IT operations workload. This involves capturing streams of continuous data, which is ideal for companies that need ways to process big data efficiently.
- *Informatica Data Replication*. Informatica can target a wide range of database and data warehouse appliances. It offers the Data Engineering product series for streaming, integration, quality and masking enterprise data. Its website features a how-to library and list of guides to help customers.
- *Talend Open Studio for Data Integration*. One of the most prominent open source data integration products, it includes a large repertoire of resources for those just getting started with the software. Talend offers tutorials, demos and blog posts on topics like the use of metadata and best practices for data model design best practices. There is also a community of experienced users that new users can reach out to for tips on using Talend's data integration solution.
- *Quest SharePlex*. This offering focuses mainly on Oracle database replication. It offers both on-premises and cloud solutions for Oracle database replication. Shareplex promises high availability, 24/7 customer support and a simple user experience that allows for quick replication and scaling.


### 140. What is a view in a relational database?

A view is a virtual table that is based on the result of a SELECT statement. It does not store data itself, but rather provides a way to access data from one or more tables in a specific way.

### 141. What is a stored procedure in a relational database?

A stored procedure is a pre-compiled collection of SQL statements that can be executed with a single call. They are useful for encapsulating logic and for improving performance by reducing network traffic and parsing overhead.

### 142. What is a trigger in a relational database?

A trigger is a set of instructions that are automatically executed in response to certain events, such as the insertion of a new row or the update of an existing row. They are useful for enforcing business rules and for maintaining data integrity.

### 143. How do you backup and restore a relational database?

There are several methods for backing up and restoring a relational database, including full backups, incremental backups, and log backups. The specific method used will depend on the database management system (DBMS) being used and the requirements of the organization. Typically, a backup schedule should be established and test restores should be performed regularly to ensure the backups are working correctly.

### 144. How do you monitor and optimize the performance of a relational database?

Performance monitoring and optimization of a relational database involves tracking key performance metrics such as response time, CPU and memory usage, and disk I/O. The database can be optimized by fine-tuning the configuration settings, creating indexes, and optimizing the SQL queries. Additionally, regular maintenance tasks such as index defragmentation, statistics update and table partition can also improve the performance.

### 145. What is the difference between a clustered index and a non-clustered index?

A clustered index determines the physical order of data in a table, while a non-clustered index creates a separate object that contains the indexed data along with a pointer to the actual data row. A table can have only one clustered index, but multiple non-clustered indexes.

### 146. What is the difference between a subquery and a join?

A subquery is a query nested within another query that is used to filter the results of the outer query. A join is a query that combines rows from two or more tables based on a related column between them.

### 147. What is a transaction in a relational database?

A transaction is a unit of work that is executed against a relational database management system (RDBMS). A transaction is a sequence of one or more SQL statements that are executed as a single unit of work. The main goal of a transaction is to maintain the integrity of the data by ensuring that all the statements within the transaction are executed successfully or none of them are executed at all.

### 148. What is Database Concurrency 
Database concurrency is a unique characteristic enabling two or more users to retrieve information from the database at the same time without affecting data integrity.


### 149. Name database concurrency problems
- *Dirty read:* This issue arises when a particular transaction accesses a data object written or updated by another uncommitted transaction in the database. 

- *Lost data updates:* This issue emerges when two transactions simultaneously operate on the same data variable, resulting in a loss of data updates made by one of the transactions. The second transaction generally nullifies the data updates of the first transaction.

- *Unrepeatable read:* This issue happens when a transaction accesses a particular database variable two or more times, but it reads a unique value of the variable on every iteration.

- *Phantom read*: This issue emerges when two identical queries get executed during a transaction, but the number of records returned by the second query is dissimilar to the first query. It happens because another transaction inserts new records in the database table before the second query runs. 

### 150. Types of concurrency database control techniques


- *Lock-based protocols: *In multi-user databases, require every transaction to request an appropriate lock before data read or write operations to prevent data integrity issues. A lock merely denotes the type of operations (read and write) permitted on a particular data object. Shared and exclusive locks are typically active to prevent data integrity problems during concurrent database transactions.
- *Timestamp-based protocols: *In multi-user databases, ensure the concurrent transactions execute in an ordered manner based on the timestamps assigned to them. Older transactions are given priority while deciding the execution order of concurrent transactions in this method.
- *Multiversion concurrency control (MVCC):* Databases like Oracle and Postgres utilize multi-version concurrency control to eliminate data consistency issues evident in simultaneous transactions. It helps eliminate the read and write operation conflicts arising during concurrent transactions. MVCC is typically used with other concurrency control mechanisms for better results, such as multiversion timestamp ordering and multiversion two-phase locking.


### 151. What are Parallel databases ?

Parallel database systems use  multiple CPUs and Disks in Parallel to improve the performance through parallelization of various operations such as loading data ,building indexes, and evaluating queries. 

### 152. What are different types of Parallel databases architecture ?

- *Shared Memory* - Primary Memory is shared through interconnection Network

- *Shared Disk* - Hard Disk or Secondary Memory is shared  through interconnection Network

- *Shared Nothing* - Individual systems are connected through interconnection Network

### 153.     What are advantages and disadvantages of shared memory ?

- Advantages -​

    It is closer to conventional machine ,
    Easy to program
    overhead is low.
    OS services are leveraged to utilize the additional CPUs.

- Disadvantage:

    It leads to bottleneck problem
    Expensive to build
    It is less sensitive to partitioning


### 154. What are advantages and disadvantages of  shared disk  architecture ?

- Advantages:

    It is closer to conventional machine ,
    Easy to program
    overhead is low.
    OS services are leveraged to utilize the additional CPUs.

- Disadvantages:

    More interference.
    Increases N/W band width.
    Shared disk less sensitive to partitioning.


### 155.  What are advantages and disadvantages of shared nothing  architecture ?
- Advantages:

    It provides linear scale up & linear speed up
    Shared nothing benefits from "good" partitioning
    Cheap to build

- Disadvantage

    Hard to program.
    Addition of new nodes requires reorganizing.


### 156. Which type of architecture supports scaling ?

Shared Nothing

### 157. Which architecture faces the problem of bottleneck ?

Shared Memory

### 158. Which type of architecture has maximum fault tolerance ?

Shared Disk

### 159. What is inter query parallelism ?

When queries within a transaction or in multiple transactions  are processed in parallel to increase CPU performance and throughput time , it is called  interquery parallelism.eg We may have 10 people to execute 10 tasks so as to increase the performance and reduce the time taken to complete the job. 

### 160. What is Linear Speedup and sublinear speedup  in Parallel database ?

Adding more CPU  increases the performance of the system  in Parallel databases up to a threshold value after that adding more CPU gives SubLinear Speedup. This scenario is similar to adding more people in a project. If we keep on adding people who are working on a single project then after a certain threshold value results may not be the same as expected as performance of the system may deteriorate due to overhead communications and other unforeseen issues.

### 161. What is Linear Scale up and sublinear scale up  in Parallel database ?

Adding more nodes   increases the performance of the system  in Parallel databases up to a threshold value after that adding more nodes  gives SubLinear Speedup.

### 162. What do you mean by SQL injection?

Black-hat hackers use the SQL injection technique that hacks the data from databases or tables. 

### 163. Explain the terms database and DBMS. Also, mention the different types of DBMS.

A software application that interacts with databases, applications, and users to capture and analyze the required data. The data stored in the database can be retrieved, deleted and modified based on the client’s requirement.

The different types of DBMS are as follows:

    Relational DBMS (RDBMS): This type of DBMS, uses a structure which allows the users to access data in relation to another piece of data in a database. In this type of DBMS, data is stored in the form of tables.
    Hierarchical DBMS:  As the name suggests, this type of DBMS has a structure similar to that of a tree, wherein the nodes represent records and the branches of the tree represent fields.
    Network DBMS: This type of DBMS supports many-to-many relations wherein multiple member records can be linked.
    Object-oriented DBMS: Uses small individual software called object to store pieces of data and the instructions for the actions to be done with the data.

### 164. What do you understand by query optimization?

Query optimization is the phase that identifies a plan for evaluation query that has the least estimated cost. This phase comes into the picture when there are a lot of algorithms and methods to execute the same task.

The advantages of query optimization are as follows:

    The output is provided faster
    A larger number of queries can be executed in less time
    Reduces time and space complexity

### 165. Do we consider NULL values the same as that of blank space or zero? 

A NULL value is not at all same as that of zero or a blank space. The NULL value represents a value which is unavailable, unknown, assigned or not applicable whereas zero is a number and blank space is a character.

### 166. What is a checkpoint in DBMS and when does it occur?

A checkpoint is a mechanism where all the previous logs are removed from the system and are permanently stored on the storage disk.  So, basically, checkpoints are those points from where the transaction log record can be used to recover all the committed data up to the point of crash.

Next, le us discuss one of the most commonly asked DBMS interview questions, that is:

### 167. What do you understand by Proactive, Retroactive and Simultaneous Update?

    Proactive Update: These updates are applied to the database before it becomes effective in the real-world environment.
    Retroactive Update: These retroactive updates are applied to a database after it becomes effective in the real-world environment.
    Simultaneous Update: These updates are applied to the database at the same instance of time as it becomes effective in a real-world environment.

### 168. What do you understand by cursor? Mention the different types of cursor

A cursor is a database object which helps in manipulating data, row by row and represents a result set.

The types of cursor are as follows:

    Implicit cursor: This type of cursor is declared automatically as soon as the execution of SQL takes place. Here, the user is not indicated about the declaration of the cursor.
    Explicit cursor: This type of cursor is defined by the PL/ SQL, as it handles a query in more than a single row.

### 169. Explain the terms specialization and generalization

    Specialization: Specialization is a process of defining a set of subclasses of the entity type. Here, each subclass will contain all the attributes and relationships of the parent entity. Apart from this, the subclasses may contain additional attributes and relationships specific to itself.
    Generalization: Generalization is a process of finding relations, common attributes for a particular set of entities; and finally defining a common superclass for them.

### 170. Whhat are the different integrity rules present in the DBMS?

The different integrity rules present in DBMS are as follows:

    Entity Integrity: This rule states that the value of the primary key can never be NULL. So, all the tuples in the column identified as the primary key should have a value.
    Referential Integrity: This rule states that either the value of the foreign key is NULL or it should be the primary key of any other relation.

### 171. What does Fill Factor concept mean with respect to indexes?

Fill Factor is used to mention the percentage of space left on every leaf-level page, which is packed with data. Usually, the default value is 100.

### 172.  What is Index hunting and how does it help in improving query performance?

The process of boosting a collection of indexes is known as Index hunting. This is done as indexes improve the query performance and the speed at which they are processed.

### 173. Explain what is a deadlock and mention how it can be resolved?

Deadlock is a situation which occurs when two transactions wait on a resource which is locked or other transaction holds.  Deadlocks can be prevented by making all the transactions acquire all the locks at the same instance of time. So, once deadlock occurs, the only way to cure is to abort one of the transactions and remove the partially completed work.

### 174. What are the differences between an exclusive lock and a shared lock?
- Exclusive Lock: An exclusive lock is a lock on a data item when a transaction is about to perform the write operation.
- Shared Lock: A shared lock allows more than one transaction to read the data items.
### 175. What are the differences between DROP, TRUNCATE and DELETE commands?
|DROP|	TRUNCATE	|DELETE|
|-|------------|---------|
|Used to delete a database, table or a view|	Used to delete all rows from a table	|Used to delete a row in the table|
|Data cannot be rollbacked|	Data cannot be rollbacked	Data can be rollbacked|
|A DDL command	|A DDL command|	A DML command.|
|Slower than TRUNCATE|	Faster than DROP and DELETE	Slower than TRUNCATE|
|Deletes the full structure of the table	|Preserves the structure of the table 	|Deletes the structure of the row from a table|

### 176. Mention the differences between UNION and UNION ALL

- UNION	: Combines the result of two or more SELECT statements consisting of distinct values	
- UNION	ALL: Combines the result set of two or more SELECT statements consisting of duplicate values

### 177. What do you understand by CLAUSE in SQL?

CLAUSE in SQL is used to limit the result set by mentioning a condition to the query. So, you can use a CLAUSE to filter rows from the entire set of records.

### 178. Mention few case manipulation functions in SQL

There are three case manipulation functions in SQL, namely:

LOWER: This function returns the string in lowercase. It takes a string as an argument and returns it by converting it into lower case.

Syntax:  LOWER(‘string’)

UPPER: This function returns the string in uppercase. It takes a string as an argument and returns it by converting it into uppercase.

Syntax:  UPPER(‘string’)

INITCAP: This function returns the string with the first letter in uppercase and the rest of the letters in lowercase.



### 179. Write a query to create a duplicate table with and without data present?
- 1: CREATE TABLE DuplicateCustomer AS SELECT * FROM Customers
- 2: CREATE TABLE DuplicateCustomer AS SELECT * FROM Customers WHERE 1=2;

### 180. Define Aggregate functions.

Functions which operate against a collection of values and returning single value is called aggregate functions

### 181. What is a Multimedia Database?

It is a special type of Database capable of storing and managing multimedia information, such as audio, video, images, etc, along with traditional text-based data. 
Some DBMS that support Multimedia are:
    MongoDB GridFS
     
    MySQL
     
    PostgreSQL
     
    IBM DB2 Content Manager
     
    Oracle Multimedia
     
    Microsoft SQL Server etc.

### 182. What is a BLOB in a multimedia database?

A BLOB (binary large object) is a special data type in relational database management systems that stores large chunks of multimedia information directly in a table in the form of a contiguous sequence of bytes.

### 183. What is adaptive bitrate streaming?

Online streaming platforms serve multimedia of varying qualities depending on the network condition of the user endpoint, and they do so by encoding files in multiple qualities or bitrates and dynamically changing as the network conditions change.

### 184. What is a deductive database 
is a database system that can make deductions (i.e. conclude additional facts) based on rules and facts stored in the (deductive) database. Datalog is the language typically used to specify facts, rules, and queries in deductive databases. A deductive database can be defined as an advanced database augmented with an inference system.
Database + Inference = Deductive database

### 185. What is spatial Data
Spatial data is any type of data that directly or indirectly references a specific geographical area or location. Sometimes called geospatial data or geographic information, spatial data can also numerically represent a physical object in a geographic coordinate system. 

### 186.  Name spatial Data Types
- Geometric data is a spatial data type that is mapped on a two-dimensional flat surface. An example is the geometric data in floor plans. Google Maps is an application that uses geometric data to provide accurate direction. In fact, it is one of the simplest examples of spatial data in action.

- Geographic data is information mapped around a sphere. Most often, the sphere is planet earth. Geographic data highlights the latitude and longitude relationships to a specific object or location. A familiar example of geographic data is a global positioning system.
### 187.  What is a Spatial Database
Spatial databases are built to store and provide powerful query capabilities for spatial data. Spatial data is often much larger in size than traditional data because of its additional locational component. Spatial databases make the storage of complex spatial data possible. Traditional database management systems are not capable of storing, querying, and indexing spatial data. 

### 188. Name some Spatial DBMS
- Esri Geodatabases: Geodatabase is the enterprise storage solution from the largest GIS vendor Esri; the industry leader in spatial data! Geodatabases were first touted as a simple geometry storage model for Esri users. 
- PostGIS:  is one of the most well known and complete spatial databases around. It is an extension to the open-source database, PostgreSQL. 
- Snowflake: Designed purely for the cloud, this unique Data Warehouse as a service platform holds the power to bring all your data together. On this platform, your data is ready for analysis at any scale, on any cloud platform you desire. 
- Oracle: Oracle Spatial permits spatial data compatibility. It is included in Oracle’s converged database by default. Similar to PostGIS, Oracle Spatial provides support for more than just vector data.
- SQL SERVER: Spatial support comes with Microsoft SQL Server, supporting a variety of data types. Vectors are the main focus of this spatial database. 
### 189. What is Active Database?
Active Database is a database consisting of set of triggers. These databases are very difficult to be maintained because of the complexity that arises in understanding the effect of these triggers. In such database, DBMS initially verifies whether the particular trigger specified in the statement that modifies the database) is activated or not, prior to executing the statement.
An active database is a database that includes an event-driven architecture (often in the form of ECA rules) which can respond to conditions both inside and outside the database. Possible uses include security monitoring, alerting, statistics gathering and authorization.
If the trigger is active then DBMS executes the condition part and then executes the action part only if the specified condition is evaluated to true. It is possible to activate more than one trigger within a single statement.
### 190.  What are NoSQL DATABASES?
are non-tabular databases and store data differently than relational tables. NoSQL databases come in a variety of types based on their data model. The main types are document, key-value, wide-column, and graph. They provide flexible schemas and scale easily with large amounts of data and high user loads. 
### 191. Types of NoSQL Databases?
- Document databases: store data in documents similar to JSON (JavaScript Object Notation) objects. Each document contains pairs of fields and values. The values can typically be a variety of types including things like strings, numbers, booleans, arrays, or objects.
- Key-value databases: are a simpler type of database where each item contains keys and values.
- Wide-column stores: store data in tables, rows, and dynamic columns.
- Graph databases: store data in nodes and edges. Nodes typically store information about people, places, and things, while edges store information about the relationships between the nodes.

### 192. Name some Document Based DBMS
    Amazon DocumentDB
    MongoDB
    Cosmos DB
    ArangoDB
    Couchbase Server
    CouchDB
### 193. Name some Key-value  Based DBMS
    Couchbase: It permits SQL-style querying and searching for text.
    Amazon DynamoDB: The key-value database which is mostly used is Amazon DynamoDB as it is a trusted database used by a large number of users. It can easily handle a large number of requests every day and it also provides various security options.
    Riak: It is the database used to develop applications.
    Aerospike: It is an open-source and real-time database working with billions of exchanges.
    Berkeley DB: It is a high-performance and open-source database providing scalability.
### 194.  Name some Wide-column stores  Based DBMS
A wide-column database is a NoSQL database that organizes data storage into flexible columns that can be spread across multiple servers or database nodes, using multi-dimensional mapping to reference data by column, row, and timestamp.
    Apache Accumulo
    Apache Cassandra
    Apache HBase
    Bigtable
    DataStax Enterprise (uses Apache Cassandra)
    DataStax Astra DB (uses Apache Cassandra)
    Hypertable
    Azure Tables
    Scylla (database)

### 195.  Name some Graph Based DBMS
A graph database (GDB) is a database that uses graph structures for storing data. It uses nodes, edges, and properties instead of tables or documents to represent and store data. The edges represent relationships between the nodes. This helps in retrieving data more easily and, in many cases, with one operation. Graph databases are commonly referred to as a NoSQL.
    Neo4J
    TigerGraph
    AWS Neptune

### 196. What is CAP (consistency, availability, partition)
The CAP theorem states that a distributed system can only provide two of three properties simultaneously: consistency, availability, and partition tolerance. The theorem formalizes the tradeoff between consistency and availability when there’s a partition.

A distributed system is a collection of computers that work together to form a single computer for end users. All of the distributed machines have one shared state and operate concurrently. With distributed systems, users must be able to communicate with any of the distributed machines without knowing it’s only one machine. The distributed system network stores its data on more than just a single node, using multiple physical or virtual machines at the same time.

- Consistency: In a consistent system, all nodes see the same data simultaneously. If we perform a read operation on a consistent system, it should return the value of the most recent write operation. The read should cause all nodes to return the same data. All users see the same data at the same time, regardless of the node they connect to. When data is written to a single node, it is then replicated across the other nodes in the system.
- Availability: When availability is present in a distributed system, it means that the system remains operational all of the time. Every request will get a response regardless of the individual state of the nodes. This means that the system will operate even if there are multiple nodes down. Unlike a consistent system, there’s no guarantee that the response will be the most recent write operation.
- Partition tolerance: When a distributed system encounters a partition, it means that there’s a break in communication between nodes. If a system is partition-tolerant, the system does not fail, regardless of whether messages are dropped or delayed between nodes within the system. To have partition tolerance, the system must replicate records across combinations of nodes and networks. 

### 197. What is BASE properties
The BASE properties of a database management system are a set of principles that guide the design and operation of modern databases.  The acronym BASE stands for Basically Available, Soft State, and Eventual Consistency.
BASE databases are used in modern, highly-available, and scalable systems that handle large amounts of data. Examples of such systems include online shopping websites, social media platforms, and cloud-based services. 

- Basically Available: This property refers to the fact that the database system should always be available to respond to user requests, even if it cannot guarantee immediate access to all data. The database may experience brief periods of unavailability, but it should be designed to minimize downtime and provide quick recovery from failures.
- Soft State: This property refers to the fact that the state of the database can change over time, even without any explicit user intervention. This can happen due to the effects of background processes, updates to data, and other factors. The database should be designed to handle this change gracefully, and ensure that it does not lead to data corruption or loss.
- Eventual Consistency: This property refers to the eventual consistency of data in the database, despite changes over time. In other words, the database should eventually converge to a consistent state, even if it takes some time for all updates to propagate and be reflected in the data. This is in contrast to the immediate consistency required by traditional ACID-compliant databases.
### 198. What is ACID properties
The ACID transaction model ensures that all performed transactions will result in reliable and consistent databases. This suits best for businesses which use OLTP (Online Transaction Processing) for IT-Systems such like ERP- or CRM-Systems. Furthermore, it can also be a good choice for OLAP (Online Analytical Processing) which is used in Data Warehouses. These applications need backend database systems which can handle many small- or medium-sized transactions occurring simultaneous by many users. An interrupted transaction with write-access must be removed from the database immediately as it could cause negative side effects impacting the consistency(e.g., vendors could be deleted although they still have open purchase orders or financial payments could be debited from one account and due to technical failure, never credited to another).
The properties of ACID are being applied for databases in order to fulfill enterprise requirements of reliability and consistency.


- Atomicity: Each transaction is either properly executed completely or does not happen at all. If the transaction was not finished the process reverts the database back to the state before the transaction started. This ensures that all data in the database is valid even if we execute big transactions which include multiple statements (e. g. SQL) composed into one transaction updating many data rows in the database. If one statement fails, the entire transaction will be aborted, and hence, no changes will be made.
- Consistency: Databases are governed by specific rules defined by table formats (data types) and table relations as well as further functions like triggers. The consistency of data will- stay reliable if transactions never endanger the structural integrity of the database. Therefor, it is not allowed to save data of different types into the same single column, to use written primary key values again or to delete data from a table which is strictly related to data in another table.
- Isolation: Databases are multi-user systems where multiple transactions happen at the same time. With Isolation, transactions cannot compromise the integrity of other transactions by interacting with them while they are still in progress. It guarantees data tables will be in the same states with several transactions happening concurrently as they happen sequentially.
- Durability: The data related to the completed transaction will persist even in cases of network or power outages. Databases that guarante Durability save data inserted or updated permanently, save all executed and planed transactions in a recording and ensure availability of the data committed via transaction even after a power failure or other system failures If a transaction fails to complete successfully because of a technical failure, it will not transform the targeted data.
