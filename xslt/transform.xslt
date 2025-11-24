<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/weather">
    <html>
      <body>
        <h2>Weather Report for <xsl:value-of select="location"/></h2>
        <p>Temperature: <xsl:value-of select="temperature"/></p>
        <p>Humidity: <xsl:value-of select="humidity"/></p>
        <p>Condition: <xsl:value-of select="condition"/></p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>