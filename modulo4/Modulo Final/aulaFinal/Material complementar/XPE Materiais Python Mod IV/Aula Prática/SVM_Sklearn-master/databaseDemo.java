import java.sql.*;
class Demo
{
	public static void main(String abc[])
	{
		try
		{
			Class.forName("oracle.jdbc.driver.ORacleDriver)");
			Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","8488");
			Statement st=con.createStatement();
			ResultSet rs=st.executeQuery("select * from student_data");
			System.out.println("Display all Records");
			System.out.println("Roll no\t Student\t Name\t Course");
			while(rs.next())		//Returns boolean value after checking existence of records
			{
				System.out.print(rs.getInt(1));
				System.out.print("\t"+rs.getString(2));
				System.out.print("\t"+rs.getString(3));
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
} 