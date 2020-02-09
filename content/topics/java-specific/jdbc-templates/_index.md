---
title: JDBC templates
ready: true
---

Both Springboot and VanillaJS require a middle man to be able to talk to a database. This is where JDBC comes in. It can be used with multiple programming languages.
Javascript languages tend to make more use of ODBC (Open Database Connectivity) whereas JDBC was created with Java in mind. The 2 are interchangeable.

Springboot has no way of directly communicating with a database, it requires a JDBC driver.

## JDBC - Java Database Connectivity

JDBC is an API that consists of interfaces used to access relational databases such as SQL.

Note: A relational database is one where the database can recognise relationships/links between the data saved in it.

JDBC allows a Java application to connect to a SQL server and run SQL scripts to work with the databases 
on the server and manipulate the tables and the data stored within them.

- [Example:](https://www.tutorialspoint.com/jdbc/jdbc-select-records.htm) Connect to a database server and fetch data from the database.

## JPA - Java Persistence API

JPA allows an individual to communicate with a database without having to create SQL queries. It bridges
the gap between SQL and Java. For instance, you can create a modal and by adding certain annotations to it, you
can create/alter the database.

[Here's](https://www.javaworld.com/article/3373652/java-persistence-with-jpa-and-hibernate-part-1-entities-and-relationships.html) a quick tutorial that outlines some of the functionality that JPA provides.

## Hibernate

JPA provides the interface (the set of rules that need to be followed). But alone it does nothing.
It needs to be implemented. This is where Hibernate comes in.

Without JPA though, Hibernate can still be used to communicate with the database in a similar manner, as can be seen
[here](https://www.tutorialspoint.com/hibernate/hibernate_examples.htm).

## Resources

- [JDBC documentation](https://www.tutorialspoint.com/jdbc/jdbc-introduction.htm).
- [Video tutorials](https://www.youtube.com/playlist?list=PLmCsXDGbJHdhs1dWrgeT1ZoitLGp90I6D).

- [JPA Documentation](https://www.tutorialspoint.com/jpa/index.htm).
- [Hibernate Documentation](https://www.tutorialspoint.com/hibernate/index.htm).

- [JPA with Hibernate video tutorials](https://www.youtube.com/watch?v=LKidsEzqwXw&list=PLgzDdh90-m_TKIz4JNuqh3QarIdKiTS3q).

Code Samples
------------

Here are examples on the syntax used to create a new table in the database.

## JDBC
```
Statement stmt = conn.createStatement();

String sql =	"CREATE TABLE User " + 
				"(id INTEGER NOT NULL, " +
				"Firstname VARCHAR(255), " +
				"Lastname VARCHAR(255))";

stmt.execureUpdate(sql);
```

## JPA

In User.java
```
@Entity
public class User
{
	@Id
	private int id;
	private String firstName;
	private String lastName;

	public class User(int id, String firstName, String lastName)
	{
		this.id = id;
		this.firstName = firstName;
		this.lastName = lastName;
	}

	public int getId()
	{
		return id;
	}

	public void setId()
	{
		this.id = id;
	}

	public String getFirstName()
	{
		return firstName;
	}

	public void setFirstName()
	{
		this.firstName = firstName;
	}

	public String getLastName()
	{
		return lastName;
	}

	public void setLastName()
	{
		this.lastName = lastName;
	}
}

```
In Persistence.xml

```
<?xml version = "1.0" encoding = "UTF-8"?>
<persistence version = "2.0" xmlns = "http://java.sun.com/xml/ns/persistence" 
   xmlns:xsi = "http://www.w3.org/2001/XMLSchema-instance" 
   xsi:schemaLocation = "http://java.sun.com/xml/ns/persistence 
   http://java.sun.com/xml/ns/persistence/persistence_2_0.xsd">
   
   <persistence-unit name = "Eclipselink_JPA" transaction-type = "RESOURCE_LOCAL">
	  <class>com.tutorialspoint.eclipselink.entity.User</class>
	  
	  <properties>
	  <property name = "javax.persistence.jdbc.url" value = "jdbc:mysql://localhost:3306/jpadb"/>
	  <property name = "javax.persistence.jdbc.user" value = "root"/>
	  <property name = "javax.persistence.jdbc.password" value = "root"/>
	  <property name = "javax.persistence.jdbc.driver" value = "com.mysql.jdbc.Driver"/>
	  <property name = "eclipselink.logging.level" value = "FINE"/>
	  <property name = "eclipselink.ddl-generation" value = "create-tables"/>
	  </properties>
   
   </persistence-unit>
</persistence>
```

## Hibernate

Hibernate also makes use of a class like the User.java class mentioned above to create a table. 
It differs from JPA by the xml file.

In hibernateContext.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<beans  xmlns="http://www.springframework.org/schema/beans"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xmlns:context="http://www.springframework.org/schema/context"
		xsi:schemaLocation="
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-4.1.xsd
		http://www.springframework.org/schema/context classpath:spring-context-4.1.xsd">
 
	<context:property-placeholder location="classpath:hibernate/persistence-sybase.properties-${env.p}.properties" />
		 
	<bean id="dataSource" destroy-method="close" class="org.apache.tomcat.dbcp.dbcp.BasicDataSource">
		<property name="driverClassName" value="${jdbc.driverClassName}" />
		<property name="url" value="${jdbc.url}" />
		<property name="username" value="${jdbc.user}" />
		<property name="password" value="${jdbc.pass}" />
	</bean>
	<bean id="hibernateProperties"
		class="org.springframework.beans.factory.config.PropertiesFactoryBean">
		<property name="properties">
			<props>
				<prop key="hibernate.dialect">${hibernate.dialect}</prop>
				<prop key="hibernate.generate_statistics">true</prop>
				<prop key="hibernate.hbm2ddl.auto">create-drop</prop>
				<prop key="hibernate.jdbc.batch_size">50</prop>
				<prop key="hibernate.show_sql">true</prop>
				<prop key="hibernate.format_sql">true</prop>
				<prop key="hibernate.id.new_generator_mappings">true</prop>
				<prop key="hibernate.cache.use_query_cache">false</prop>
				<prop key="hibernate.cache.use_second_level_cache">false</prop>
				<prop key="org.hibernate.envers.audit_table_suffix">_AUDIT</prop>
				<prop key="hibernate.cache.provider_class">org.hibernate.cache.EhCacheProvider</prop>
			</props>
		</property>
	</bean>
	<bean id="hibernateAnnotatedClasses"
		class="org.springframework.beans.factory.config.ListFactoryBean">
		<property name="sourceList">
 
			<list>
				<value>com.macq.ci.tools.entities.UcRequest</value>
			</list>
		</property>
	</bean>
 
	<bean id="persistenceExceptionTranslationPostProcessor"
		class="org.springframework.dao.annotation.PersistenceExceptionTranslationPostProcessor" />
 
	<bean id="hibernateSessionFactory"
		class="org.springframework.orm.hibernate3.annotation.AnnotationSessionFactoryBean">
		<property name="dataSource" ref="dataSource" />
		<property name="hibernateProperties" ref="hibernateProperties"></property>
		<property name="annotatedClasses" ref="hibernateAnnotatedClasses" />
		<property name="entityInterceptor">
			<bean class="com.macq.ci.tools.interceptors.UcOwnerInterceptor" />
		</property>
	</bean>
 
	<bean id="transactionManager"
		class="org.springframework.orm.hibernate3.HibernateTransactionManager">
		<property name="sessionFactory" ref="hibernateSessionFactory" />
	</bean>
 
</beans>
```




















