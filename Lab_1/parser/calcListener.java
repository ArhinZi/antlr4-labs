// Generated from calc.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link calcParser}.
 */
public interface calcListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link calcParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(calcParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link calcParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(calcParser.ExprContext ctx);
}