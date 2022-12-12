/**
 * program
 */


 public class program {
   public static void main(String[] args) { 

    String line = "empty";
    try {
        String pathProject = System.getProperty("user.dir");
           String pathFile = pathProject.concat("/file.txt");

       File file = new File(pathFile);
       if (file.createNewFile()) {
           System.out.println("file.created"); }
       else {
           BufferedReader bufReader = new BufferedReader(new FileReader(file));
           System.out.println("file.existed");
           line = bufReader.readLine();
           bufReader.close(); }
    } catch (Exception e) {
       //e.printStackTrace();
    } finally {
       System.out.println(line);
    }
    
}
}



