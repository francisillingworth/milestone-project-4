$(window).on('load', function() {
    if (!sessionStorage.getItem('shown-modal')) {
        $('#explainFeaturesModal').modal('show');
        sessionStorage.setItem('shown-modal', 'true');
    }
});
