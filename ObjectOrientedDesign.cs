public class ChessBoard
{
    private List<ChessPiece> _piecesOnBoard;
    private Player _currentPlayer;

    public ChessBoard()
    {
        this.CreatePieces();
        this.ArrangePiecesToStartingPositions();
    }

    private bool isMoveLegal(ChessPiece, start_pos, end_pos) { return true; }

    public void makeMove(ChessPiece, start_pos, end_pos)
    {
        
    }

    public bool isWinner()
    {
         return false;
    }
}

public class ChessPiece
{
    private Color _color;
    private Type _type;
}

public class Player
{
    private string _userName;
    private Color _color;
    private List<ChessPiece> _piecesOnBoard;
}

public class ChessGameManager
{
    private ChessBoard _board;
    private Player _player_1;
    private Player _player_2;

    private Player _currentPlayer;
}
