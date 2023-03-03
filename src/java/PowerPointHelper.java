import org.apache.poi.sl.usermodel.TableCell;
import org.apache.poi.sl.usermodel.TextParagraph;
import org.apache.poi.xslf.usermodel.XSLFSlide;
import org.apache.poi.xslf.usermodel.XSLFTable;
import org.apache.poi.xslf.usermodel.XSLFTableCell;
import org.apache.poi.xslf.usermodel.XSLFTableRow;
import org.apache.poi.xslf.usermodel.XSLFTextParagraph;
import org.apache.poi.xslf.usermodel.XSLFTextRun;

import java.awt.*;

public class PowerPointHelper {

  public XSLFTable creationOfTable(XSLFSlide slide) {

    XSLFTable table = slide.createTable();
    table.setAnchor(new Rectangle(50, 50, 450, 300));

    int numColumns = 3;
    int numRows = 5;

    // header
    XSLFTableRow headerRow = table.addRow();
    headerRow.setHeight(50);
    for (int i = 0; i < numColumns; i++) {
      XSLFTableCell th = headerRow.addCell();
      XSLFTextParagraph p = th.addNewTextParagraph();
      p.setTextAlign(TextParagraph.TextAlign.CENTER);
      XSLFTextRun r = p.addNewTextRun();
      r.setText("HeaderPart " + (i + 1));
      r.setBold(true);
      r.setFontColor(Color.white);
      th.setFillColor(new Color(79, 129, 189));
      th.setBorderWidth(TableCell.BorderEdge.bottom, 2.0);
      th.setBorderColor(TableCell.BorderEdge.bottom, Color.white);
      // all columns are equally sized
      table.setColumnWidth(i, 150);
    }

    return table;
  }
}
