package org.linkedin.in.discovery.service;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class DbConnection {

  public String getResult() {
    Connection connection = null;
    try {
      // below two lines are used for connectivity.
      Class.forName("com.mysql.cj.jdbc.Driver");
      connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "mydbuser", "mydbuser");

      // mydb is database
      // mydbuser is name of database
      // mydbuser is password of database

      Statement statement;
      statement = connection.createStatement();
      ResultSet resultSet;
      resultSet = statement.executeQuery("select * from designation");
      int code;
      String title = null;
      while (resultSet.next()) {
        code = resultSet.getInt("code");
        title = resultSet.getString("title").trim();
        System.out.println("Code : " + code + " Title : " + title);
      }
      return title;
    } catch (SQLException e) {
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
    }
    return null;
  }

  public String getResults() {
    String res = getResult();
    return res.toLowerCase();
  }
}
